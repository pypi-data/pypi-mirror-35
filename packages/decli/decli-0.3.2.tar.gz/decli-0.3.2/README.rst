======
Decli
======

Minimal declarative cli tool.

.. image:: https://img.shields.io/travis/Woile/decli.svg?style=flat-square
    :alt: Travis
    :target: https://travis-ci.org/Woile/decli

.. image:: https://img.shields.io/codecov/c/github/Woile/decli.svg?style=flat-square
    :alt: Codecov
    :target: https://codecov.io/gh/Woile/decli

.. image:: https://img.shields.io/pypi/v/decli.svg?style=flat-square
    :alt: PyPI
    :target: https://pypi.org/project/decli/

.. image:: https://img.shields.io/pypi/pyversions/decli.svg?style=flat-square
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/decli/


.. code-block:: python

    from decli import cli

    data = {
        "prog": "myapp",
        "description": "Process some integers.",
        "arguments": [
            {
                "name": "integers",
                "metavar": "N",
                "type": int,
                "nargs": "+",
                "help": "an integer for the accumulator",
            },
            {
                "name": "--sum",
                "dest": "accumulate",
                "action": "store_const",
                "const": sum,
                "default": max,
                "help": "sum the integers (default: find the max)",
            },
        ],
    }
    parser = cli(data)
    parser.parse_args()


::

    >> parser.print_help()
    usage: myapp [-h] [--sum] N [N ...]

    Process some integers.

    positional arguments:
    N           an integer for the accumulator

    optional arguments:
    -h, --help  show this help message and exit
    --sum       sum the integers (default: find the max)


::

    In [4]: args = parser.parse_args("--sum 3 2 1".split())

    In [5]: args.accumulate(args.integers)
    Out[5]: 6


.. contents::
    :depth: 2


About
=====

Decli is minimal wrapper around **argparse**.

It's useful when writing big applications that have many arguments and subcommands, this way it'll be more clear.

It's a minimal library to rapidly create an interface separated from your app.

It's possible to use any argument from **argparse** and it works really well with it.

Forget about copy pasting the argparse functions, if you are lazy like me, this library should be really handy!

Many cases were tested, but it's possible that not everything was covered, so if you find anything, please report it.


Installation
============

::

    pip install -U decli

or alternatively:

::

    poetry add decli


Usage
======

Main cli
--------

Create the dictionary in which the cli tool is declared.

The same arguments argparse use are accepted, except parents, which is ignored.

- prog - The name of the program (default: sys.argv[0])
- usage - The string describing the program usage (default: generated from arguments added to parser)
- description - Text to display before the argument help (default: none)
- epilog - Text to display after the argument help (default: none)
- formatter_class - A class for customizing the help output
- prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)
- fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)
- argument_default - The global default value for arguments (default: None)
- conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)
- add_help - Add a -h/--help option to the parser (default: True)
- allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)

More info in the `argparse page <https://docs.python.org/3/library/argparse.html#argumentparser-objects>`_

Example:

.. code-block:: python

    data = {
        "prog": "myapp",
        "description": "This app does something cool",
        "epilog": "And that's it"
    }


Arguments
---------

It's just a list with dictionaries. To add aliases just use a list instead of a string.

Accepted values:


- name: - Either a name or a list of option strings, e.g. foo or -f, --foo.
- action - The basic type of action to be taken when this argument is encountered at the command line.
- nargs - The number of command-line arguments that should be consumed.
- const - A constant value required by some action and nargs selections.
- default - The value produced if the argument is absent from the command line.
- type - The type to which the command-line argument should be converted.
- choices - A container of the allowable values for the argument.
- required - Whether or not the command-line option may be omitted (optionals only).
- help - A brief description of what the argument does.
- metavar - A name for the argument in usage messages.
- dest - The name of the attribute to be added to the object returned by parse_args().


More info about `arguments <https://docs.python.org/3/library/argparse.html#the-add-argument-method>`_

Example:

.. code-block:: python

    data = {
        "prog": "myapp",
        "description": "This app does something cool",
        "epilog": "And that's it",
        "arguments": [
            {
                "name": "--foo"
            },
            {
                "name": ["-b", "--bar"]
            }
        ]
    }


Subcommands
-----------

Just a dictionary where the most important key is **commands** which is a list of the commands.


Accepted values:


- title - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments
- description - description for the sub-parser group in help output, by default None
- commands - list of dicts describing the commands. Same arguments as the **main cli** are supported. And **func** which is really important.
- prog - usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments before the subparser argument
- action - the basic type of action to be taken when this argument is encountered at the command line
- dest - name of the attribute under which sub-command name will be stored; by default None and no value is stored
- required - Whether or not a subcommand must be provided, by default False.
- help - help for sub-parser group in help output, by default None
- metavar - string presenting available sub-commands in help; by default it is None and presents sub-commands in form {cmd1, cmd2, ..}


More info about `subcommands <https://docs.python.org/3/library/argparse.html#sub-commands>`_

Func
~~~~

Usually in a sub-command it's useful to specify to which function are they pointing to. That's why each command should have this parameter.


When you are building an app which does multiple things, each function should be mapped to a command this way, using the **func** argument.

Example:

.. code-block:: python

    from decli import cli

    data = {
        "prog": "myapp",
        "description": "This app does something cool",
        "epilog": "And that's it",
        "subcommands": {
            "commands": [
                {
                    "name": "sum",
                    "help": "new project",
                    "func": sum,
                    "arguments": [
                        {
                            "name": "integers",
                            "metavar": "N",
                            "type": int,
                            "nargs": "+",
                            "help": "an integer for the accumulator",
                        },
                        {"name": "--name", "nargs": "?"},
                    ],
                }
            ]
        }
    }

    parser = cli(data)
    args = parser.parse_args(["sum 1 2 3".split()])
    args.func(args.integers)  # Runs the sum of the integers


Recipes
=======

Subcommands
-----------------

.. code-block:: python

    from decli import cli

    data = {
        "prog": "myapp",
        "formatter_class": argparse.RawDescriptionHelpFormatter,
        "description": "The software does this and that",
        "epilog": "This is the epilooogpoe  ",
        "arguments": [
            {
                "name": "--debug",
                "action": "store_true",
                "default": False,
                "help": "use debug mode",
            },
            {
                "name": ["-v", "--version"],
                "action": "store_true",
                "default": False,
                "help": "get the installed version",
            },
        ],
        "subcommands": {
            "title": "main",
            "description": "main commands",
            "commands": [
                {
                    "name": "all",
                    "help": "check every values is true",
                    "func": all
                },
                {
                    "name": ["s", "sum"],
                    "help": "new project",
                    "func": sum,
                    "arguments": [
                        {
                            "name": "integers",
                            "metavar": "N",
                            "type": int,
                            "nargs": "+",
                            "help": "an integer for the accumulator",
                        },
                        {"name": "--name", "nargs": "?"},
                    ],
                }
            ],
        },
    }
    parser = cli(data)
    args = parser.parse_args(["sum 1 2 3".split()])
    args.func(args.integers)  # Runs the sum of the integers


Minimal
-------

This app does nothing, but it's the min we can have:

.. code-block:: python

    from decli import cli

    parser = cli({})
    parser.print_help()

::

    usage: ipython [-h]

    optional arguments:
    -h, --help  show this help message and exit


Positional arguments
--------------------

.. code-block:: python

    from decli import cli

    data = {
        "arguments": [
            {
                "name": "echo"
            }
        ]
    }
    parser = cli(data)
    args = parser.parse_args(["foo"])

::

    In [11]: print(args.echo)
    foo


Positional arguments with type
------------------------------

When a type is specified, the argument will be treated as that type, otherwise it'll fail.

.. code-block:: python

    from decli import cli

    data = {
        "arguments": [
            {
                "name": "square",
                "type": int
            }
        ]
    }
    parser = cli(data)
    args = parser.parse_args(["1"])

::

    In [11]: print(args.echo)
    1

Optional arguments
------------------

.. code-block:: python

    from decli import cli

    data = {
        "arguments": [
            {
                "name": "--verbose",
                "help": "increase output verbosity"
            }
        ]
    }
    parser = cli(data)
    args = parser.parse_args(["--verbosity 1"])

::

    In [11]: print(args.verbosity)
    1

    In [15]: args = parser.parse_args([])

    In [16]: args
    Out[16]: Namespace(verbose=None)


Short options
-------------

Used to add short versions of the options

.. code-block:: python

    data = {
        "arguments": [
            {
                "name": ["-v", "--verbose"],
                "help": "increase output verbosity"
            }
        ]
    }


Combining Positional and Optional arguments
-------------------------------------------

.. code-block:: python

    data = {
        "arguments": [
            {
                "name": "square",
                "type": int,
                "help": "display a square of a given number"
            },
            {
                "name": ["-v", "--verbose"],
                "action": "store_true",
                "help": "increase output verbosity"
            }
        ]
    }
    parser = cli(data)

    args = parser.parse_args()
    answer = args.square**2
    if args.verbose:
        print("the square of {} equals {}".format(args.square, answer))
    else:
        print(answer)


More Examples
=============

Many examples from `argparse documentation <https://docs.python.org/3/library/argparse.htm>`_
are covered in test/examples.py


Testing
=======

1. Clone the repo
2. Install dependencies

::

    poetry install

3. Run tests

::

    poetry run pytest -s --cov-report term-missing --cov=decli tests/


Contributing
============

**PRs are welcome!**
