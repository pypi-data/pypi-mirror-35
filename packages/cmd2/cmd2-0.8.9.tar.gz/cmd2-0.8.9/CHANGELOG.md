## 0.8.9 (August TBD, 2018)
* Bug Fixes
    * Fixed extra slash that could print when tab completing users on Windows

## 0.8.8 (June 28, 2018)
* Bug Fixes
    * Prevent crashes that could occur attempting to open a file in non-existent directory or with very long filename
* Enhancements
    * ``display_matches`` is no longer restricted to delimited strings

## 0.8.7 (May 28, 2018)
* Bug Fixes
    * Make sure pip installs version 0.8.x if you have python 2.7

## 0.8.6 (May 27, 2018)
* Bug Fixes
    * Commands using the @with_argparser_and_unknown_args were not correctly recognized when tab completing
    * Fixed issue where completion display function was overwritten when a submenu quits
    * Fixed ``AttributeError`` on Windows when running a ``select`` command cause by **pyreadline** not implementing ``remove_history_item``
* Enhancements
    * Added warning about **libedit** variant of **readline** not being supported on macOS
    * Added tab-completion of alias names in value filed of **alias** command
    * Enhanced the ``py`` console in the following ways
        * Added tab completion of Python identifiers instead of **cmd2** commands
        * Separated the ``py`` console history from the **cmd2** history

## 0.8.5 (April 15, 2018)
* Bug Fixes
    * Fixed a bug with all argument decorators where the wrapped function wasn't returning a value and thus couldn't cause the cmd2 app to quit

* Enhancements
    * Added support for verbose help with -v where it lists a brief summary of what each command does
    * Added support for categorizing commands into groups within the help menu
        * See the [Grouping Commands](http://cmd2.readthedocs.io/en/latest/argument_processing.html?highlight=verbose#grouping-commands) section of the docs for more info
        * See [help_categories.py](https://github.com/python-cmd2/cmd2/blob/master/examples/help_categories.py) for an example
    * Tab completion of paths now supports ~user user path expansion
    * Simplified implementation of various tab completion functions so they no longer require ``ctypes``
    * Expanded documentation of ``display_matches`` list to clarify its purpose. See cmd2.py for this documentation.
    * Adding opening quote to tab completion if any of the completion suggestions have a space.

* **Python 2 EOL notice**
    * This is the last release where new features will be added to ``cmd2`` for Python 2.7
    * The 0.9.0 release of ``cmd2`` will support Python 3.4+ only
    * Additional 0.8.x releases may be created to supply bug fixes for Python 2.7 up until August 31, 2018
    * After August 31, 2018 not even bug fixes will be provided for Python 2.7

## 0.8.4 (April 10, 2018)
* Bug Fixes
    * Fixed conditional dependency issue in setup.py that was in 0.8.3.

## 0.8.3 (April 09, 2018)
* Bug Fixes
    * Fixed ``help`` command not calling functions for help topics
    * Fixed not being able to use quoted paths when redirecting with ``<`` and ``>``

* Enhancements
    * Tab completion has been overhauled and now supports completion of strings with quotes and spaces.
    * Tab completion will automatically add an opening quote if a string with a space is completed.
    * Added ``delimiter_complete`` function for tab completing delimited strings
    * Added more control over tab completion behavior including the following flags. The use of these flags is documented in cmd2.py
        * ``allow_appended_space``
        * ``allow_closing_quote``
    * Due to the tab completion changes, non-Windows platforms now depend on [wcwidth](https://pypi.python.org/pypi/wcwidth).
    * An alias name can now match a command name.
    * An alias can now resolve to another alias.

* Attribute Changes (Breaks backward compatibility)
    * ``exclude_from_help`` is now called ``hidden_commands`` since these commands are hidden from things other than help, including tab completion
        * This list also no longer takes the function names of commands (``do_history``), but instead uses the command names themselves (``history``)
    * ``excludeFromHistory`` is now called ``exclude_from_history``
    * ``cmd_with_subs_completer()`` no longer takes an argument called ``base``. Adding tab completion to subcommands has been simplified to declaring it in the
    subcommand parser's default settings. This easily allows arbitrary completers like path_complete to be used.
    See [subcommands.py](https://github.com/python-cmd2/cmd2/blob/master/examples/subcommands.py) for an example of how to use
    tab completion in subcommands. In addition, the docstring for ``cmd_with_subs_completer()`` offers more details.


## 0.8.2 (March 21, 2018)

* Bug Fixes
    * Fixed a bug in tab-completion of command names within sub-menus
    * Fixed a bug when using persistent readline history in Python 2.7
    * Fixed a bug where the ``AddSubmenu`` decorator didn't work with a default value for ``shared_attributes``
    * Added a check to ``ppaged()`` to only use a pager when running in a real fully functional terminal
* Enhancements
    * Added [quit_on_sigint](http://cmd2.readthedocs.io/en/latest/settingchanges.html#quit-on-sigint) attribute to enable canceling current line instead of quitting when Ctrl+C is typed
    * Added possibility of having readline history preservation in a SubMenu
    * Added [table_display.py](https://github.com/python-cmd2/cmd2/blob/master/examples/table_display.py) example to demonstrate how to display tabular data
    * Added command aliasing with ``alias`` and ``unalias`` commands
    * Added the ability to load an initialization script at startup
        * See [alias_startup.py](https://github.com/python-cmd2/cmd2/blob/master/examples/alias_startup.py) for an example
    * Added a default SIGINT handler which terminates any open pipe subprocesses and re-raises a KeyboardInterrupt
    * For macOS, will load the ``gnureadline`` module if available and ``readline`` if not

## 0.8.1 (March 9, 2018)

* Bug Fixes
    * Fixed a bug if a non-existent **do_*** method was added to the ``exclude_from_help`` list
    * Fixed a bug in a unit test which would fail if your home directory was empty on a Linux system
    * Fixed outdated help text for the **edit** command
    * Fixed outdated [remove_unused.py](https://github.com/python-cmd2/cmd2/blob/master/examples/remove_unused.py)
* Enhancements
    * Added support for sub-menus.
        * See [submenus.py](https://github.com/python-cmd2/cmd2/blob/master/examples/submenus.py) for an example of how to use it
    * Added option for persistent readline history
        * See [persistent_history.py](https://github.com/python-cmd2/cmd2/blob/master/examples/persistent_history.py) for an example
        * See the [Searchable command history](http://cmd2.readthedocs.io/en/latest/freefeatures.html#searchable-command-history) section of the documentation for more info
    * Improved PyPI packaging by including unit tests and examples in the tarball
    * Improved documentation to make it more obvious that **poutput()** should be used instead of **print()**
    * ``exclude_from_help`` and ``excludeFromHistory`` are now instance instead of class attributes
    * Added flag and index based tab completion helper functions
        * See [tab_completion.py](https://github.com/python-cmd2/cmd2/blob/master/examples/tab_completion.py)
    * Added support for displaying output which won't fit on the screen via a pager using ``ppaged()``
        * See [paged_output.py](https://github.com/python-cmd2/cmd2/blob/master/examples/paged_output.py)
* Attributes Removed (**can cause breaking changes**)
    * ``abbrev`` - Removed support for abbreviated commands
        * Good tab completion makes this unnecessary and its presence could cause harmful unintended actions
    * ``case_insensitive`` - Removed support for case-insensitive command parsing
        * Its presence wasn't very helpful and could cause harmful unintended actions

## 0.8.0 (February 1, 2018)
* Bug Fixes
    * Fixed unit tests on Python 3.7 due to changes in how re.escape() behaves in Python 3.7
    * Fixed a bug where unknown commands were getting saved in the history
* Enhancements
    * Three new decorators for **do_*** commands to make argument parsing easier
        * **with_argument_list** decorator to change argument type from str to List[str]
            * **do_*** commands get a single argument which is a list of strings, as pre-parsed by shlex.split()
        * **with_arparser** decorator for strict argparse-based argument parsing of command arguments
            * **do_*** commands get a single argument which is the output of argparse.parse_args()
        * **with_argparser_and_unknown_args** decorator for argparse-based argument parsing, but allows unknown args
            * **do_*** commands get two arguments, the output of argparse.parse_known_args()
    *  See the [Argument Processing](http://cmd2.readthedocs.io/en/latest/argument_processing.html) section of the documentation for more information on these decorators
        * Alternatively, see the [argparse_example.py](https://github.com/python-cmd2/cmd2/blob/master/examples/argparse_example.py)
        and [arg_print.py](https://github.com/python-cmd2/cmd2/blob/master/examples/arg_print.py) examples
    * Added support for Argparse sub-commands when using the **with_argument_parser** or **with_argparser_and_unknown_args** decorators
        * See [subcommands.py](https://github.com/python-cmd2/cmd2/blob/master/examples/subcommands.py) for an example of how to use subcommands
        * Tab-completion of sub-command names is automatically supported
    * The **__relative_load** command is now hidden from the help menu by default
        * This command is not intended to be called from the command line, only from within scripts
    * The **set** command now has an additional **-a/--all** option to also display read-only settings
    * The **history** command can now run, edit, and save prior commands, in addition to displaying prior commands.
    * The **history** command can now automatically generate a transcript file for regression testing
        * This makes creating regression tests for your ``cmd2`` application trivial
* Commands Removed
    * The **cmdenvironment** has been removed and its functionality incorporated into the **-a/--all** argument to **set**
    * The **show** command has been removed.  Its functionality has always existing within **set** and continues to do so
    * The **save** command has been removed. The capability to save commands is now part of the **history** command.
    * The **run** command has been removed. The capability to run prior commands is now part of the **history** command.
* Other changes
    * The **edit** command no longer allows you to edit prior commands. The capability to edit prior commands is now part of the **history** command. The **edit** command still allows you to edit arbitrary files.
    * the **autorun_on_edit** setting has been removed.
    * For Python 3.4 and earlier, ``cmd2`` now has an additional dependency on the ``contextlib2`` module
* Deprecations
    * The old **options** decorator for optparse-based argument parsing is now *deprecated*
        * The old decorator is still present for now, but will be removed in a future release
        * ``cmd2`` no longer includes **optparse.make_option**, so if your app needs it import directly from optparse

## 0.7.9 (January 4, 2018)

* Bug Fixes
    * Fixed a couple broken examples
* Enhancements
    * Improved documentation for modifying shortcuts (command aliases)
    * Made ``pyreadline`` a dependency on Windows to ensure tab-completion works
* Other changes
    * Abandoned official support for Python 3.3.  It should still work, just don't have an easy way to test it anymore.

## 0.7.8 (November 8, 2017)

* Bug Fixes
    * Fixed ``poutput()`` so it can print an integer zero and other **falsy** things
    * Fixed a bug which was causing autodoc to fail for building docs on Readthedocs
    * Fixed bug due to ``pyperclip`` dependency radically changing its project structure in latest version
* Enhancements
    * Improved documentation for user-settable environment parameters
    * Improved documentation for overriding the default supported comment styles
    * Added ``runcmds_plus_hooks()`` method to run multiple commands w/o a cmdloop

## 0.7.7 (August 25, 2017)

* Bug Fixes
    * Added workaround for bug which occurs in Python 2.7 on Linux when ``pygtk`` is installed
    * ``pfeedback()`` now honors feedback_to_output setting and won't redirect when it is ``False``
    * For ``edit`` command, both **editor** and **filename** can now have spaces in the name/path
    * Fixed a bug which occurred when stdin was a pipe instead of a tty due to input redirection
* Enhancements
    * ``feedback_to_output`` now defaults to ``False`` so info like command timing won't redirect
    * Transcript regular expressions now have predictable, tested, and documented behavior
        * This makes a breaking change to the format and expectations of transcript testing
        * The prior behavior removed whitespace before making the comparison, now whitespace must match exactly
        * Prior version did not allow regexes with whitespace, new version allows any regex
    * Improved display for ``load`` command and input redirection when **echo** is ``True``

## 0.7.6 (August 11, 2017)

* Bug Fixes
    * Case-sensitive command parsing was completely broken and has been fixed
    * ``<Ctrl>+d`` now properly quits when case-sensitive command parsing is enabled
    * Fixed some pyperclip clipboard interaction bugs on Linux
    * Fixed some timing bugs when running unit tests in parallel by using monkeypatch
* Enhancements
    * Enhanced tab-completion of cmd2 command names to support case-insensitive completion
    * Added an example showing how to remove unused commands
    * Improved how transcript testing handles prompts with ANSI escape codes by stripping them
    * Greatly improved implementation for how command output gets piped to a shell command

## 0.7.5 (July 8, 2017)

* Bug Fixes
    * `case_insensitive` is no longer a runtime-settable parameter, but it was still listed as such
    * Fixed a recursive loop bug when abbreviated commands are enabled and it could get stuck in the editor forever
        * Added additional command abbreviations to the "exclude from history" list
    * Fixed argparse_example.py and pirate.py examples and transcript_regex.txt transcript
    * Fixed a bug in a unit test which occurred under unusual circumstances
* Enhancements
    * Organized all attributes used to configure the ParserManager into a single location
    * Set the default value of `abbrev` to `False` (which controls whether or not abbreviated commands are allowed)
        * With good tab-completion of command names, using abbreviated commands isn't particularly useful
        * And it can create complications if you are't careful
    * Improved implementation of `load` to use command queue instead of nested inner loop

## 0.7.4 (July 3, 2017)

* Bug fixes
    * Fixed a couple bugs in interacting with pastebuffer/clipboard on macOS and Linux
    * Fixed a couple bugs in edit and save commands if called when history is empty
    * Ability to pipe ``cmd2`` command output to a shell command is now more reliable, particularly on Windows
    * Fixed a bug in ``pyscript`` command on Windows related to ``\`` being interpreted as an escape
* Enhancements
    * Ensure that path and shell command tab-completion results are alphabetically sorted
    * Removed feature for load command to load scripts from URLS
        * It didn't work, there were no unit tests, and it felt out of place
    * Removed presence of a default file name and default file extension
        * These also strongly felt out of place
        * ``load`` and ``_relative_load`` now require a file path
        * ``edit`` and ``save`` now use a temporary file if a file path isn't provided
    * ``load`` command has better error checking and reporting
    * Clipboard copy and paste functionality is now handled by the **pyperclip** module
    * ``shell`` command now supports redirection and piping of output
    * Added a lot of unit tests
* Other changes
    * Removed pause command
    * Added a dependency on the **pyperclip** module

## 0.7.3 (June 23, 2017)

* Bug fixes
    * Fixed a bug in displaying a span of history items when only an end index is supplied
    * Fixed a bug which caused transcript test failures to display twice
* Enhancements
    * Added the ability to exclude commands from the help menu (**eof** included by default)
    * Redundant **list** command removed and features merged into **history** command
    * Added **pyscript** command which supports tab-completion and running Python scripts with arguments
    * Improved tab-completion of file system paths, command names, and shell commands
        * Thanks to Kevin Van Brunt for all of the help with debugging and testing this
    * Changed default value of USE_ARG_LIST to True - this affects the beavhior of all **@options** commands
        * **WARNING**: This breaks backwards compatibility, to restore backwards compatibility, add this to the
          **__init__()** method in your custom class derived from cmd2.Cmd:
            * cmd2.set_use_arg_list(False)
        * This change improves argument parsing for all new applications
    * Refactored code to encapsulate most of the pyparsing logic into a ParserManager class

## 0.7.2 (May 22, 2017)

* Added a MANIFEST.ini file to make sure a few extra files get included in the PyPI source distribution

## 0.7.1 (May 22, 2017)

* Bug fixes
    * ``-`` wasn't being treated as a legal character
    * The allow_cli_args attribute wasn't properly disabling parsing of args at invocation when False
    * py command wasn't allowing scripts which used *cmd* function prior to entering an interactive Python session
    * Don't throw exception when piping output to a shell command
    * Transcript testing now properly calls ``preloop`` before and ``postloop`` after
    * Fixed readline bug related to ANSI color escape codes in the prompt
* Added CONTRIBUTING.md and CODE_OF_CONDUCT.md files
* Added unicode parsing unit tests and listed unicode support as a feature when using Python 3
* Added more examples and improved documentation
    * Example for how use cmd2 in a way where it doesn't own the main loop so it can integrate with external event loops
    * Example for how to use argparse for parsing command-line args at invocation
    * Example for how to use the **py** command to run Python scripts which use conditional control flow
    * Example of how to use regular expressions in a transcript test
* Added CmdResult namedtumple for returning and storing results
* Added local file system path completion for ``edit``, ``load``, ``save``, and ``shell`` commands
* Add shell command completion for ``shell`` command or ``!`` shortcut
* Abbreviated multiline commands are no longer allowed (they never worked correctly anyways)

## 0.7.0 (February 23, 2017)

* Refactored to use six module for a unified codebase which supports both Python 2 and Python 3
* Stabilized on all platforms (Windows, Mac, Linux) and all supported Python versions (2.7, 3.3, 3.4, 3.5, 3.6, PyPy)
* Added lots of unit tests and fixed a number of bugs
* Improved documentation and moved it to cmd2.readthedocs.io


## 0.6.9 (October 3, 2016)

* Support Python 3 input()
* Fix subprocess.mswindows bug
* Add Python3.6 support
* Drop distutils from setup.py


## 0.6.8 (December 9, 2014)

* better editor checking (by Ian Cordascu)


## 0.6.6.1 (August 14, 2013)

* No changes to code trunk.  Generated sdist from Python 2.7 to avoid 2to3 changes being applied to source.  (Issue https://bitbucket.org/catherinedevlin/cmd2/issue/6/packaging-bug)


## 0.6.6 (August 6, 2013)

* Added fix by bitbucket.org/desaintmartin to silence the editor check.  bitbucket.org/catherinedevlin/cmd2/issue/1/silent-editor-check


## 0.6.5.1 (March 18, 2013)

* Bugfix for setup.py version check for Python 2.6, contributed by Tomaz Muraus (https://bitbucket.org/kami)


## 0.6.5 (February 29, 2013)

* Belatedly began a NEWS.txt
* Changed pyparsing requirement for compatibility with Python version (2 vs 3)
