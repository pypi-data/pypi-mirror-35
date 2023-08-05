# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['decli']

package_data = \
{'': ['*'],
 'decli': ['.pytest_cache/*', '.pytest_cache/v/*', '.pytest_cache/v/cache/*']}

setup_kwargs = {
    'name': 'decli',
    'version': '0.4.0',
    'description': 'Minimal, easy-to-use, declarative cli tool',
    'long_description': '======\nDecli\n======\n\nMinimal declarative cli tool.\n\n.. image:: https://img.shields.io/travis/Woile/decli.svg?style=flat-square\n    :alt: Travis\n    :target: https://travis-ci.org/Woile/decli\n\n.. image:: https://img.shields.io/codecov/c/github/Woile/decli.svg?style=flat-square\n    :alt: Codecov\n    :target: https://codecov.io/gh/Woile/decli\n\n.. image:: https://img.shields.io/pypi/v/decli.svg?style=flat-square\n    :alt: PyPI\n    :target: https://pypi.org/project/decli/\n\n.. image:: https://img.shields.io/pypi/pyversions/decli.svg?style=flat-square\n    :alt: PyPI - Python Version\n    :target: https://pypi.org/project/decli/\n\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "prog": "myapp",\n        "description": "Process some integers.",\n        "arguments": [\n            {\n                "name": "integers",\n                "metavar": "N",\n                "type": int,\n                "nargs": "+",\n                "help": "an integer for the accumulator",\n            },\n            {\n                "name": "--sum",\n                "dest": "accumulate",\n                "action": "store_const",\n                "const": sum,\n                "default": max,\n                "help": "sum the integers (default: find the max)",\n            },\n        ],\n    }\n    parser = cli(data)\n    parser.parse_args()\n\n\n::\n\n    >> parser.print_help()\n    usage: myapp [-h] [--sum] N [N ...]\n\n    Process some integers.\n\n    positional arguments:\n    N           an integer for the accumulator\n\n    optional arguments:\n    -h, --help  show this help message and exit\n    --sum       sum the integers (default: find the max)\n\n\n::\n\n    In [4]: args = parser.parse_args("--sum 3 2 1".split())\n\n    In [5]: args.accumulate(args.integers)\n    Out[5]: 6\n\n\n.. contents::\n    :depth: 2\n\n\nAbout\n=====\n\nDecli is minimal wrapper around **argparse**.\n\nIt\'s useful when writing big applications that have many arguments and subcommands, this way it\'ll be more clear.\n\nIt\'s a minimal library to rapidly create an interface separated from your app.\n\nIt\'s possible to use any argument from **argparse** and it works really well with it.\n\nForget about copy pasting the argparse functions, if you are lazy like me, this library should be really handy!\n\nMany cases were tested, but it\'s possible that not everything was covered, so if you find anything, please report it.\n\n\nInstallation\n============\n\n::\n\n    pip install -U decli\n\nor alternatively:\n\n::\n\n    poetry add decli\n\n\nUsage\n======\n\nMain cli\n--------\n\nCreate the dictionary in which the cli tool is declared.\n\nThe same arguments argparse use are accepted, except parents, which is ignored.\n\n- prog - The name of the program (default: sys.argv[0])\n- usage - The string describing the program usage (default: generated from arguments added to parser)\n- description - Text to display before the argument help (default: none)\n- epilog - Text to display after the argument help (default: none)\n- formatter_class - A class for customizing the help output\n- prefix_chars - The set of characters that prefix optional arguments (default: ‘-‘)\n- fromfile_prefix_chars - The set of characters that prefix files from which additional arguments should be read (default: None)\n- argument_default - The global default value for arguments (default: None)\n- conflict_handler - The strategy for resolving conflicting optionals (usually unnecessary)\n- add_help - Add a -h/--help option to the parser (default: True)\n- allow_abbrev - Allows long options to be abbreviated if the abbreviation is unambiguous. (default: True)\n\nMore info in the `argparse page <https://docs.python.org/3/library/argparse.html#argumentparser-objects>`_\n\nExample:\n\n.. code-block:: python\n\n    data = {\n        "prog": "myapp",\n        "description": "This app does something cool",\n        "epilog": "And that\'s it"\n    }\n\n\nArguments\n---------\n\nIt\'s just a list with dictionaries. To add aliases just use a list instead of a string.\n\nAccepted values:\n\n\n- name: - Either a name or a list of option strings, e.g. foo or -f, --foo.\n- action - The basic type of action to be taken when this argument is encountered at the command line.\n- nargs - The number of command-line arguments that should be consumed.\n- const - A constant value required by some action and nargs selections.\n- default - The value produced if the argument is absent from the command line.\n- type - The type to which the command-line argument should be converted.\n- choices - A container of the allowable values for the argument.\n- required - Whether or not the command-line option may be omitted (optionals only).\n- help - A brief description of what the argument does.\n- metavar - A name for the argument in usage messages.\n- dest - The name of the attribute to be added to the object returned by parse_args().\n\n\nMore info about `arguments <https://docs.python.org/3/library/argparse.html#the-add-argument-method>`_\n\nExample:\n\n.. code-block:: python\n\n    data = {\n        "prog": "myapp",\n        "description": "This app does something cool",\n        "epilog": "And that\'s it",\n        "arguments": [\n            {\n                "name": "--foo"\n            },\n            {\n                "name": ["-b", "--bar"]\n            }\n        ]\n    }\n\n\nSubcommands\n-----------\n\nJust a dictionary where the most important key is **commands** which is a list of the commands.\n\n\nAccepted values:\n\n\n- title - title for the sub-parser group in help output; by default “subcommands” if description is provided, otherwise uses title for positional arguments\n- description - description for the sub-parser group in help output, by default None\n- commands - list of dicts describing the commands. Same arguments as the **main cli** are supported. And **func** which is really important.\n- prog - usage information that will be displayed with sub-command help, by default the name of the program and any positional arguments before the subparser argument\n- action - the basic type of action to be taken when this argument is encountered at the command line\n- dest - name of the attribute under which sub-command name will be stored; by default None and no value is stored\n- required - Whether or not a subcommand must be provided, by default False.\n- help - help for sub-parser group in help output, by default None\n- metavar - string presenting available sub-commands in help; by default it is None and presents sub-commands in form {cmd1, cmd2, ..}\n\n\nMore info about `subcommands <https://docs.python.org/3/library/argparse.html#sub-commands>`_\n\nFunc\n~~~~\n\nUsually in a sub-command it\'s useful to specify to which function are they pointing to. That\'s why each command should have this parameter.\n\n\nWhen you are building an app which does multiple things, each function should be mapped to a command this way, using the **func** argument.\n\nExample:\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "prog": "myapp",\n        "description": "This app does something cool",\n        "epilog": "And that\'s it",\n        "subcommands": {\n            "commands": [\n                {\n                    "name": "sum",\n                    "help": "new project",\n                    "func": sum,\n                    "arguments": [\n                        {\n                            "name": "integers",\n                            "metavar": "N",\n                            "type": int,\n                            "nargs": "+",\n                            "help": "an integer for the accumulator",\n                        },\n                        {"name": "--name", "nargs": "?"},\n                    ],\n                }\n            ]\n        }\n    }\n\n    parser = cli(data)\n    args = parser.parse_args(["sum 1 2 3".split()])\n    args.func(args.integers)  # Runs the sum of the integers\n\n\nRecipes\n=======\n\nSubcommands\n-----------------\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "prog": "myapp",\n        "formatter_class": argparse.RawDescriptionHelpFormatter,\n        "description": "The software does this and that",\n        "epilog": "This is the epilooogpoe  ",\n        "arguments": [\n            {\n                "name": "--debug",\n                "action": "store_true",\n                "default": False,\n                "help": "use debug mode",\n            },\n            {\n                "name": ["-v", "--version"],\n                "action": "store_true",\n                "default": False,\n                "help": "get the installed version",\n            },\n        ],\n        "subcommands": {\n            "title": "main",\n            "description": "main commands",\n            "commands": [\n                {\n                    "name": "all",\n                    "help": "check every values is true",\n                    "func": all\n                },\n                {\n                    "name": ["s", "sum"],\n                    "help": "new project",\n                    "func": sum,\n                    "arguments": [\n                        {\n                            "name": "integers",\n                            "metavar": "N",\n                            "type": int,\n                            "nargs": "+",\n                            "help": "an integer for the accumulator",\n                        },\n                        {"name": "--name", "nargs": "?"},\n                    ],\n                }\n            ],\n        },\n    }\n    parser = cli(data)\n    args = parser.parse_args(["sum 1 2 3".split()])\n    args.func(args.integers)  # Runs the sum of the integers\n\n\nMinimal\n-------\n\nThis app does nothing, but it\'s the min we can have:\n\n.. code-block:: python\n\n    from decli import cli\n\n    parser = cli({})\n    parser.print_help()\n\n::\n\n    usage: ipython [-h]\n\n    optional arguments:\n    -h, --help  show this help message and exit\n\n\nPositional arguments\n--------------------\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "arguments": [\n            {\n                "name": "echo"\n            }\n        ]\n    }\n    parser = cli(data)\n    args = parser.parse_args(["foo"])\n\n::\n\n    In [11]: print(args.echo)\n    foo\n\n\nPositional arguments with type\n------------------------------\n\nWhen a type is specified, the argument will be treated as that type, otherwise it\'ll fail.\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "arguments": [\n            {\n                "name": "square",\n                "type": int\n            }\n        ]\n    }\n    parser = cli(data)\n    args = parser.parse_args(["1"])\n\n::\n\n    In [11]: print(args.echo)\n    1\n\nOptional arguments\n------------------\n\n.. code-block:: python\n\n    from decli import cli\n\n    data = {\n        "arguments": [\n            {\n                "name": "--verbose",\n                "help": "increase output verbosity"\n            }\n        ]\n    }\n    parser = cli(data)\n    args = parser.parse_args(["--verbosity 1"])\n\n::\n\n    In [11]: print(args.verbosity)\n    1\n\n    In [15]: args = parser.parse_args([])\n\n    In [16]: args\n    Out[16]: Namespace(verbose=None)\n\n\nShort options\n-------------\n\nUsed to add short versions of the options.\n\n.. code-block:: python\n\n    data = {\n        "arguments": [\n            {\n                "name": ["-v", "--verbose"],\n                "help": "increase output verbosity"\n            }\n        ]\n    }\n\n\nGrouping\n--------\n\nThis is only possible using arguments.\n\nOnly affect the way the help gets displayed. You might be looking for subcommands.\n\n\n.. code-block:: python\n\n    data = {\n        "prog": "mycli",\n        "arguments": [\n            {\n                "name": "--save",\n                "group": "main",\n                "help": "This save belongs to the main group",\n            },\n            {\n                "name": "--remove",\n                "group": "main",\n                "help": "This remove belongs to the main group",\n            },\n        ],\n    }\n    parser = cli(data)\n    parser.print_help()\n\n::\n\n    usage: mycli [-h] [--save SAVE] [--remove REMOVE]\n\n    optional arguments:\n    -h, --help       show this help message and exit\n\n    main:\n    --save SAVE      This save belongs to the main group\n    --remove REMOVE  This remove belongs to the main group\n\n\nCombining Positional and Optional arguments\n-------------------------------------------\n\n.. code-block:: python\n\n    data = {\n        "arguments": [\n            {\n                "name": "square",\n                "type": int,\n                "help": "display a square of a given number"\n            },\n            {\n                "name": ["-v", "--verbose"],\n                "action": "store_true",\n                "help": "increase output verbosity"\n            }\n        ]\n    }\n    parser = cli(data)\n\n    args = parser.parse_args()\n    answer = args.square**2\n    if args.verbose:\n        print(f"the square of {args.square} equals {answer}")\n    else:\n        print(answer)\n\n\nMore Examples\n-------------\n\nMany examples from `argparse documentation <https://docs.python.org/3/library/argparse.html>`_\nare covered in test/examples.py\n\n\nTesting\n=======\n\n1. Clone the repo\n2. Install dependencies\n\n::\n\n    poetry install\n\n3. Run tests\n\n::\n\n    poetry run pytest -s --cov-report term-missing --cov=decli tests/\n\n\nContributing\n============\n\n**PRs are welcome!**\n',
    'author': 'Santiago Fraire',
    'author_email': 'santiwilly@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
