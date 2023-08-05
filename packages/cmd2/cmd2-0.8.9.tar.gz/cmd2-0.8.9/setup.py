#!/usr/bin/python
# coding=utf-8
"""
Setuptools setup file, used to install or test 'cmd2'
"""
import sys

import setuptools
from setuptools import setup

VERSION = '0.8.9'
DESCRIPTION = "cmd2 - a tool for building interactive command line applications in Python"
LONG_DESCRIPTION = """cmd2 is a tool for building interactive command line applications in Python. Its goal is to make
it quick and easy for developers to build feature-rich and user-friendly interactive command line applications.  It
provides a simple API which is an extension of Python's built-in cmd module.  cmd2 provides a wealth of features on top
of cmd to make your life easier and eliminates much of the boilerplate code which would be necessary when using cmd.

The latest documentation for cmd2 can be read online here:
https://cmd2.readthedocs.io/

Main features:

    - Searchable command history (`history` command and `<Ctrl>+r`)
    - Text file scripting of your application with `load` (`@`) and `_relative_load` (`@@`)
    - Python scripting of your application with ``pyscript``
    - Run shell commands with ``!``
    - Pipe command output to shell commands with `|`
    - Redirect command output to file with `>`, `>>`; input from file with `<`
    - Bare `>`, `>>` with no filename send output to paste buffer (clipboard)
    - `py` enters interactive Python console (opt-in `ipy` for IPython console)
    - Multi-line commands
    - Special-character command shortcuts (beyond cmd's `?` and `!`)
    - Settable environment parameters
    - Parsing commands with arguments using `argparse`, including support for sub-commands
    - Unicode character support (*Python 3 only*)
    - Good tab-completion of commands, sub-commands, file system paths, and shell commands
    - Python 2.7 and 3.4+ support
    - Linux, macOS and Windows support
    - Trivial to provide built-in help for all commands
    - Built-in regression testing framework for your applications (transcript-based testing)
    - Transcripts for use with built-in regression can be automatically generated from `history -t`

Usable without modification anywhere cmd is used; simply import cmd2.Cmd in place of cmd.Cmd.
"""

CLASSIFIERS = list(filter(None, map(str.strip,
"""
Development Status :: 5 - Production/Stable
Environment :: Console
Operating System :: OS Independent
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: MIT License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())))

INSTALL_REQUIRES = ['pyparsing >= 2.0.1', 'pyperclip', 'six']

EXTRAS_REQUIRE = {
    # Windows also requires pyreadline to ensure tab completion works
    ":sys_platform=='win32'": ['pyreadline'],
    ":sys_platform!='win32'": ['wcwidth'],
    # Python 3.4 and earlier require contextlib2 for temporarily redirecting stderr and stdout
    ":python_version<'3.5'": ['contextlib2'],
    # Python 3.3 and earlier require enum34 backport of enum module from Python 3.4
    ":python_version<'3.4'": ['enum34'],
    # Python 2.7 also requires subprocess32
    ":python_version<'3.0'": ['subprocess32'],
}

if int(setuptools.__version__.split('.')[0]) < 18:
    EXTRAS_REQUIRE = {}
    if sys.platform.startswith('win'):
        INSTALL_REQUIRES.append('pyreadline')
    else:
        INSTALL_REQUIRES.append('wcwidth')
    if sys.version_info < (3, 5):
        INSTALL_REQUIRES.append('contextlib2')
    if sys.version_info < (3, 4):
        INSTALL_REQUIRES.append('enum34')
    if sys.version_info < (3, 0):
        INSTALL_REQUIRES.append('subprocess32')

# unittest.mock was added in Python 3.3.  mock is a backport of unittest.mock to all versions of Python
TESTS_REQUIRE = ['mock', 'pytest', 'pytest-xdist']
DOCS_REQUIRE = ['sphinx', 'sphinx_rtd_theme', 'pyparsing', 'pyperclip', 'six']

setup(
    name="cmd2",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author='Catherine Devlin',
    author_email='catherine.devlin@gmail.com',
    url='https://github.com/python-cmd2/cmd2',
    license='MIT',
    platforms=['any'],
    py_modules=["cmd2"],
    keywords='command prompt console cmd',
    python_requires='>=2.7',
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    tests_require=TESTS_REQUIRE,
)
