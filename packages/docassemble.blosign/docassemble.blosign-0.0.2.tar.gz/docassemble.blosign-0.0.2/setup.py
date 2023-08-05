import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.blosign',
      version='0.0.2',
      description=('A docassemble extension for integrating with Blosign.'),
      long_description='# docassemble.blosign\r\n\r\nA docassemble extension that allows you to sign pdf documents with [Blosign](https://blosign.com)\r\n\r\n## Installation\r\n\r\nInstall this package from within your Docassemble package management screen.\r\n\r\n## Configuration\r\n\r\nThis package use a Personal Access Token (PAT) to authenticate with the Blosing API. See Blosign documentation for details\r\n\r\nTo configure Doccassemble to access your Blosign account, go into the configuration screen of you docassemble instance and add the following configuration lines.\r\n\r\n```\r\nblosign:\r\n  token: { Your personal access token }\r\n  test-mode: True\r\n```\r\n\r\n### Test Mode\r\nIf you set `test-mode: True`, the extension will use sandbox environment on the Blosing API.\r\n\r\nIf you set `test-mode: False`, the extension will use production environment on the Blosing API.\r\n\r\n### Usage\r\nInclude the module in your interview.\r\n\r\n```\r\n---\r\nmodules:\r\n  - docassemble.blosing.blosing\r\n---\r\n``` \r\n\r\nAsk your questions and call Blosing API:\r\n\r\n```\r\napi.request_signatures(people, document, signInOrder=False, message=None, filename=None, expiryDate=None)\r\n```\r\n\r\nYou can see an interview example on \r\n`<your docassemble>/interview?i=docassemble.blosign:data/questions/blosign_test.yml`\r\n\r\n## API Documentation\r\nVisit: https://api.blosing.com/v2/docs/\r\n',
      long_description_content_type='text/markdown',
      author='Javier Goñi',
      author_email='jgoni@porthos.com.ar',
      license='The MIT License (MIT)',
      url='https://blosign.com',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['requests>=2.27.1'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/blosign/', package='docassemble.blosign'),
     )

