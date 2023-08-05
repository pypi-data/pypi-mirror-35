# The MIT License (MIT)
#
# Copyright (c) 2017-2018 Niklas Rosenstein
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Base classes and interfaces.
"""

# Workaround because the module is not assigned as an attribute to the
# nodepy parent module yet on cyclic imports.
import sys
import nodepy.context
_context = sys.modules['nodepy.context']

from nodepy import utils
import os
import pathlib2 as pathlib
import six
import types
import weakref


class Extension(object):
  """
  This class only documents the interface that is used by the standard Node.py
  runtime and does not need to be subclassed in order to implement an
  extension. An object that provides any of the methods is sufficient (such
  as the root namespace of a module).
  """

  def init_extensions(self, package, module):
    """
    Called when the extension is loaded for a package or module (only when the
    extension is explicitly declared as an extension in the respective entity).
    """

    pass

  def preprocess_python_source(self, module, source):
    """
    Preprocess the source code of a Python module before it is executed. Must
    return the new source code string.
    """

    return source


class RequestString(object):
  """
  Represents a standard request string, which is either a relative request
  or a module request. Such request strings are usually not absolute paths.
  """

  def __init__(self, value):
    self._value = utils.as_text(value)

  def __str__(self):
    return self._value

  def __repr__(self):
    return '<RequestString value={!r}>'.format(self._value)

  def __eq__(self, other):
    if isinstance(other, six.text_type):
      return other == self._value
    elif isinstance(other, RequestString):
      return other._value == self._value
    else:
      return False

  def path(self):
    """
    Returns a #pathlib.Path for this request string. The implementation for
    #RequestString.path always raises a #RuntimeError because it is never
    absolute. This property only works on absolute requests.
    """

    if os.path.isabs(self._value):
      return pathlib.Path(self._value)
    raise RuntimeError('RequestString.path not supported.')

  def joinwith(self, path):
    """
    Join this request string with a path. Only works for non-absolute paths.
    """

    return path.joinpath(self._value)

  def is_absolute(self):
    return os.path.isabs(self._value)

  def is_relative(self):
    s = self._value
    return s in ('.', '..') or s.startswith('./') or s.startswith('../')

  def is_module(self):
    return not self.is_relative()


class RequestPath(object):
  """
  Represents a #pathlib.Path as in a #Request. Path requests are always
  considered absolute, even if the contained path is relative, because that
  relative path can only be resolved in the current working directory.
  """

  def __init__(self, path):
    if not isinstance(path, pathlib.Path):
      raise TypeError('RequestPath() expected pathlib.Path object')
    self._path = path

  def __str__(self):
    return self._path

  def __repr__(self):
    return '<RequestPath value={!r}>'.format(self._path)

  def path(self):
    return self._path

  def joinpath(self, path):
    raise RuntimeError('RequestPath.joinpath() not supported.')

  def is_absolute(self):
    return True

  def is_relative(self):
    return False

  def is_module(self):
    return False


class Request(object):
  """
  # Parameters
  context (Context)
  directory (pathlib.Path)
  string (RequestString, RequestPath)
  additional_search_path (list of str)
  """

  @staticmethod
  def is_relative_request(s):
    return s in ('.', '..') or s.startswith('./') or s.startswith('../')

  def __init__(self, context, directory, string, additional_search_path=()):
    assert isinstance(context, _context.Context), type(context)
    assert isinstance(directory, pathlib.Path), type(directory)
    assert isinstance(string, (RequestString, RequestPath)), type(string)
    self.context = context
    self.directory = directory
    self.string = string
    self.additional_search_path = additional_search_path

  def __repr__(self):
    return '<Request "{}" from "{}">'.format(self.string, self.directory)

  @property
  def related_paths(self):
    if not hasattr(self, '_related_paths'):
      self._related_paths = []
      for path in utils.path.upiter(self.directory):
        path = path.joinpath(self.context.modules_directory)
        if path.is_dir():
          self._related_paths.append(path)
    return self._related_paths


class Module(object):

  def __init__(self, context, package, filename, directory=None):
    assert isinstance(context, _context.Context) or context is None
    assert isinstance(package, Package) or package is None
    assert isinstance(filename, pathlib.Path), type(filename)
    assert isinstance(directory, pathlib.Path) or directory is None
    assert filename.is_absolute(), "Module filename must be absolute ({!r})".format(filename)
    self.context = context
    self.package = package
    self.filename = filename
    self.directory = directory or filename.parent
    self.namespace = None
    self.exports = NotImplemented
    self.loaded = False
    self.exception = None
    self.require = _context.Require(self.context, self.directory)

  def __repr__(self):
    return '<{} {!r} at "{}">'.format(type(self).__name__, self.name, self.filename)

  def create_namespace(self):
    return types.ModuleType(str(self.name))  # does not accept unicode in Python 2

  @property
  def name(self):
    """
    Returns the name of the module. If #Module.package is available, the name
    will be retrieved by creating a relative path from #Module.filename to the
    #Package.directory. If that failes, the #Module.filename's `stem` is
    returned.
    """

    if self.package:
      directory = self.package.directory
      if self.package.resolve_root:
        directory = directory.joinpath(self.package.resolve_root)
      rel = None
      try:
        rel = self.filename.with_suffix('').relative_to(directory)
      except ValueError as e:
        if self.package.resolve_root:
          # Possibly this module is required from a directory outside of
          # the package's resolve_root, and Path.relative_to() will raise a
          # ValueError if the file is not inside the specified directory.
          try:
            rel = type(self.filename)(os.path.relpath(str(self.filename.with_suffix('')), str(directory)))
          except ValueError as e:
            pass  # On a different drive
        pass
      if rel:
        parts = filter(bool, utils.path.lparts(rel))
        return self.package.name + '/' + '/'.join(parts)

    return self.filename.stem

  def init(self):
    """
    Called to initialize the #Module.namespace and reset #Module.exports
    and should be used from #Module.load() before the actual module content
    is loaded.
    """

    self.loaded = False
    self.exports = NotImplemented
    self.exception = None
    self.namespace = self.create_namespace()
    self.namespace.__file__ = str(self.filename)
    self.namespace.module = self
    self.namespace.require = self.require

  def load(self):
    """
    Implemented by subclass. Loads the contents of the module.

    Use #Context.load_module() instead of calling this method directly for
    the standard behaviour and integrity checks (also calls #init()).
    """

    raise NotImplementedError


class Package(object):
  """
  A package is a container for #Module#s and usually represents a physical
  directory on the filesystem that contains a metadata file.

  # Parameters

  directory (pathlib.Path):
    The directory that is this package.

  payload (dict):
    A dictionary that represents the Package metadata in the standard package
    metadata format as defined by the `nodepy.json` specification. The
    following keys are used by the Node.py runtime:

    * `name`
    * `main` (defaults to `"index"`)
    * `extensions` (defaults to an empty list)
    * `resolve_root` (defaults to #None)
  """

  def __init__(self, context, directory, payload):
    assert isinstance(directory, pathlib.Path)

    if 'name' not in payload:
      msg = 'invalid package payload for "{}": no "name" field'
      raise ValueError(msg.format(directory))

    self.context = context
    self.directory = directory
    self.payload = payload
    self.require = _context.Require(context, directory)

  def __repr__(self):
    return '<Package {!r} at "{}">'.format(self.name, self.directory)

  @property
  def name(self):
    return self.payload['name']

  @property
  def extensions(self):
    return self.payload.get('extensions', [])

  @property
  def resolve_root(self):
    return self.payload.get('resolve_root', '')

  @property
  def main(self):
    return self.payload.get('main', 'index')

  @property
  def is_main_defined(self):
    return bool(self.payload.get('main'))


class Resolver(object):
  """
  Interface for objects that can resolve requests for modules.
  """

  def resolve_module(self, request):
    raise NotImplementedError


class ResolveError(Exception):

  def __init__(self, request, search_paths=None, linked_paths=None):
    self.request = request
    self.search_paths = search_paths or []
    self.linked_paths = linked_paths or []

  def append_from(self, other):
    for path in other.search_paths:
      if path not in self.search_paths:
        self.search_paths.append(path)
    for path in other.linked_paths:
      if path not in self.linked_paths:
        self.linked_paths.append(path)

  def __str__(self):
    lines = [str(self.request.string)]
    if self.search_paths:
      lines.append('  searched in:')
      for path in self.search_paths:
        lines.append('    - {}'.format(path))
    if self.linked_paths:
      lines.append('  followed links to:')
      for path in self.linked_paths:
        lines.append('    - {}'.format(path))
    return '\n'.join(lines)


class PathAugmentor(object):
  """
  Interface for objects that can convert from one type of #pathlib.Path
  to another. This is used, for example, to implement the support of loading
  Node.py modules from ZIP files.
  """

  def augment_path(self, path):
    raise NotImplementedError


class ZipPathAugmentor(PathAugmentor):

  def augment_path(self, path):
    try:
      return utils.path.zippath.make(path)
    except ValueError:
      return path
