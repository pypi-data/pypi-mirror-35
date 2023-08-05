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
Standard extensions usually available to Node.py instances.
"""

from nodepy import base
import re


class ImportSyntax(base.Extension):
  """
  This extension preprocess Python source code to replace a new form of the
  import syntax with valid Python code.

  # Examples

  ```python
  import 'module'             # Just import, no name assigned
  import 'module' as default_member
  import default_member from 'module'
  import {some_member} from 'module'
  import {some_member as new_name} from 'module'
  import {foo, bar, spam, egg} from 'module'
  import * from 'module'
  import default_member, * from 'module'

  # Importing members from the module's namespace instead of from the
  # members of the exported object:
  import {{some_hidden_member}} from 'module'

  # Assign to another member already in the scope.
  import existing_member.foo from 'module'

  # Multiline supported
  import {some_member}
    from 'module'
  ```
  """

  _re_import_as = re.compile(
    r'''^(?P<indent>[^\S\n]*)import\s+(?P<q>"|')(?P<mod>.*?)(?P=q)(?:\s+as\s+(?P<n>[\.\w]+))?[^\S\n]*$''',
    re.M
  )
  _re_import_from = re.compile(
    r'''
    ^(?P<indent>[^\S\n]*)     # Keep track of the indentation level
    import\s+
    (?P<members>
      (?:
        [\.\w]+|              # Default member
        (?:[\.\w]+\s*,\s*)?   # Default member + specific members
      )?
      (?:
        (?:
          \{\{[^}]+\}\}|      # Specific members, not from exports
          \*                  # Starred-import
        )
        |(?:
          \{[^}]+\}|          # Specific members
          \*                  # Starred-import
        )
      )?
    )\s+
    from\s+
    (?P<q>["'])(?P<mod>.*)(?P=q)[^\S\n]*$
    ''',
    re.M | re.X
  )
  _regexes = [(_re_import_as, 'as'), (_re_import_from, 'from')]

  @staticmethod
  def __import_symbols_from_stmt(module, symbols, exports=True):
    if exports:
      stmt = '_reqres=require({!r});'.format(module)
    else:
      stmt = '_reqres=require({!r}, exports=False).namespace;'.format(module)
    for name in symbols:
      alias = name = name.strip()
      parts = re.split('\s+', name)
      if len(parts) == 3 and parts[1] == 'as':
        name, __, alias = parts
      stmt += '{0}=_reqres.{1};'.format(alias, name)
    return stmt + 'del _reqres'

  def preprocess_python_source(self, module, source):
    while True:
      for regex, kind in self._regexes:
        match = regex.search(source)
        if match: break
      else:
        break

      if kind == 'as':
        as_name = match.group('n')
        if as_name:
          repl = '{}=require({!r})'.format(as_name, match.group('mod'))
        else:
          repl = 'require({!r})'.format(match.group('mod'))
      elif kind == 'from':
        module = match.group('mod')
        members = match.group('members')
        if members == '*':
          repl = 'require.star({!r})'.format(module)
        elif '{' in members:

          # Handle brace-enclosed import of members, optionally preceeded by
          # a default-member import.
          if members.startswith('{'):
            default_name = None
          else:
            default_name, members = members.partition(',')[::2]
            members = members.lstrip()
            assert members.startswith('{')
          assert members.endswith('}')
          members = members[1:-1]

          # Second pair of braces indicates import from the module namespace
          # instead of the exported object.
          if members.startswith('{'):
            exports = False
            assert members.endswith('}')
            members = members[1:-1]
          else:
            exports = True

          repl = self.__import_symbols_from_stmt(module, members.split(','), exports)
          if default_name:
            repl = '{}=require({!r});'.format(default_name, module) + repl
        elif members.endswith('*') and members.count(',') == 1:
          default_member = members.split(',')[0].strip()
          repl = 'require.star({0!r}); {1}=require({0!r})'.format(module, default_member)
        else:
          repl = '{}=require({!r})'.format(members, module)
      else:
        raise RuntimeError

      # Add additional newlines to the replacement until it spans
      # the same number of newlines than the matched sequence. This
      # is to keep error message more consistent.
      repl = match.group('indent') + repl + '\n' * match.group(0).count('\n')

      source = source[:match.start()] + repl + source[match.end():]

    return source
