#!/usr/bin/env python
"""Generate zsh completion script.

Usage
-----
.. code-block:: zsh
    scripts/zsh_completion.py
    sudo mv _[^_]* /usr/share/zsh/site-functions  # don't mv __pycache__
    rm -f ~/.zcompdump  # optional
    compinit  # regenerate ~/.zcompdump

Debug
-----
.. code-block:: zsh
    scripts/zsh_completion.py MODULE_NAME -  # will output to stdout

Refer
-----
- https://github.com/ytdl-org/youtube-dl/blob/master/devscripts/zsh-completion.py
- https://github.com/zsh-users/zsh/blob/master/Etc/completion-style-guide
- https://gist.githubusercontent.com/zeroSteiner/215953f2fe54ed75e8159125fabe2aba/raw/d746c8da027b738b16118ee4313d048c9f60aa11/zpycompletion.py

Examples
--------
.. code-block::
    '(- *)'{-h,--help}'[show this help message and exit]'
    |<-1->||<---2--->||<---------------3--------------->|

.. code-block:: console
    % foo --<TAB>
    option
    --help      show this help message and exit
    % foo --help <TAB>
    no more arguments

.. code-block::
    --color'[When to show color. Default: auto. Support: auto, always, never]:when:(auto always never)'
    |<-2->||<------------------------------3------------------------------->||<4>||<--------5-------->|

.. code-block:: console
    % foo --color <TAB>
    when
    always
    auto
    never

.. code-block::
    --color'[When to show color. Default: auto. Support: auto, always, never]:when:((auto\:"only when output is stdout" always\:always never\:never))'
    |<-2->||<------------------------------3------------------------------->||<4>||<--------------------------------5------------------------------->|

.. code-block:: console
    % foo --color <TAB>
    when
    always   always
    auto     only when output is stdout
    never    never

.. code-block::
    --config='[Config file. Default: ~/.config/foo/foo.toml]:config file:_files -g *.toml'
    |<--2-->||<---------------------3--------------------->||<---4---->||<------5------->|

.. code-block:: console
    % foo --config <TAB>
    config file
    a.toml  b/ ...
    ...

.. code-block::
    {1,2}'::_command_names -e'
    |<2->|4|<-------5------->|

.. code-block:: console
    % foo help<TAB>
    _command_names -e
    help2man  generate a simple manual page
    helpviewer
    ...
    % foo hello hello <TAB>
    no more arguments

.. code-block::
    '*: :_command_names -e'
    2|4||<-------5------->|

.. code-block:: console
    % foo help<TAB>
    external command
    help2man  generate a simple manual page
    helpviewer
    ...
    % foo hello hello help<TAB>
    external command
    help2man  generate a simple manual page
    helpviewer
    ...

+----+------------+----------+------+
| id | variable   | required | expr |
+====+============+==========+======+
| 1  | prefix     | F        | (.*) |
| 2  | optionstr  | T        | .*   |
| 3  | helpstr    | F        | [.*] |
| 4  | metavar    | F        | :.*  |
| 5  | completion | F        | :.*  |
+----+------------+----------+------+
"""
from argparse import (
    FileType,
    SUPPRESS,
    _HelpAction,
    _SubParsersAction,
    _VersionAction,
)
import os
from os.path import dirname as dirn
import sys
from typing import Final, TYPE_CHECKING, Tuple

from setuptools import find_packages

if TYPE_CHECKING:
    from argparse import Action

rootpath = dirn(dirn(os.path.abspath(__file__)))
path = os.path.join(rootpath, "src")
packages = find_packages(path)
if packages == []:
    path = rootpath
    packages = find_packages(path)
sys.path.insert(0, path)
PACKAGES: Final = packages
PACKAGE: Final = PACKAGES[0] if sys.argv[1:2] == [] else sys.argv[1]
parser = __import__(PACKAGE).build_parser()
actions = parser._actions
BINNAME: Final = PACKAGE.replace("_", "-")
BINNAMES: Final = [BINNAME]
ZSH_COMPLETION_FILE: Final = (
    "_" + BINNAME if sys.argv[2:3] == [] else sys.argv[2]
)
ZSH_COMPLETION_TEMPLATE: Final = os.path.join(
    dirn(os.path.abspath(__file__)), "zsh_completion.in"
)
SUPPRESS_HELP = SUPPRESS
SUPPRESS_USAGE = SUPPRESS

case_template = """\
      '{{metavar}}')
        _arguments -s -S \\
          {{flags}}
        ;;
"""
subparser = ""
commands = []
cases = []


def generate_flag(action: "Action") -> str:
    """generate_flag.

    :param action:
    :type action: "Action"
    :rtype: str
    """
    if action.__class__ in [_HelpAction, _VersionAction]:
        prefix = "'(- : *)'"
    elif isinstance(action, _SubParsersAction):
        prefix = ""
    else:
        prefix = ""

    if len(action.option_strings) > 1:  # {} cannot be quoted
        optionstr = "{" + ",".join(action.option_strings) + "}'"
    elif len(action.option_strings) == 1:
        optionstr = action.option_strings[0] + "'"
    elif isinstance(action, _SubParsersAction):
        optionstr = "'"
    else:  # action.option_strings == [], positional argument
        if action.nargs in ["*", "+"]:
            optionstr = "'*"  # * must be quoted
        else:
            if isinstance(action.nargs, int) and action.nargs > 1:
                optionstr = "{" + "," * (action.nargs - 1) + "}'"
            else:  # action.nargs in [1, None, "?"]:
                optionstr = "'"

    if (
        action.help
        and action.help != SUPPRESS_HELP
        and action.option_strings != []
    ):
        helpstr = action.help.replace("]", "\\]").replace("'", "'\\''")
        helpstr = "[" + helpstr + "]"
    else:
        helpstr = ""

    if isinstance(action.metavar, str):
        metavar = action.metavar
    elif isinstance(action.metavar, Tuple):
        metavar = " ".join(map(str, action.metavar))
        # need some changes in template file
    else:  # action.metavar is None
        if action.nargs == 0:
            metavar = ""
        elif action.option_strings == []:
            metavar = action.dest
        elif isinstance(action.type, FileType):
            metavar = "file"
        elif action.type:
            metavar = action.type.__name__
        else:
            metavar = action.default.__class__.__name__
    if metavar != "":
        # use lowcase conventionally
        metavar = metavar.lower().replace(":", "\\:")

    if isinstance(action, _SubParsersAction):
        # need some changes in template file
        completion = "->" + metavar
        metavar = " "
    elif metavar == "marker":
        from plotext._utility import marker_codes, hd_symbols

        marker_codes.update(hd_symbols)
        choices = map("\\:".join, marker_codes.items())
        completion = "((" + " ".join(map(str, choices)) + "))"
    elif action.choices:
        if metavar == "color":
            from plotext.plotext_cli import color_choices

            choices = []
            for color_choice in color_choices:
                if color_choice[-1] == "+":
                    color_choice += "\\:clearer"
                choices += [color_choice]
            completion = "((" + " ".join(map(str, choices)) + "))"
        else:
            completion = "(" + " ".join(map(str, action.choices)) + ")"
    elif metavar == "file":
        completion = "_files"
        metavar = " "
    elif metavar == "dir":
        completion = "_dirs"
        metavar = " "
    elif metavar == "url":
        completion = "_urls"
        metavar = " "
    elif metavar == "command":
        completion = "_command_names -e"
        metavar = " "
    else:
        completion = ""

    if metavar != "":
        metavar = ":" + metavar
    if completion != "":
        completion = ":" + completion

    flag = "{0}{1}{2}{3}{4}'".format(
        prefix, optionstr, helpstr, metavar, completion
    )
    return flag


flags = []
for action in actions:
    flag = generate_flag(action)
    flags += [flag]

    if isinstance(action, _SubParsersAction):
        subparser = flag.split(":->")[-1].strip("'")
        for subaction in action._choices_actions:
            if isinstance(subaction.metavar, str):
                metavar = subaction.metavar
            elif isinstance(subaction.metavar, Tuple):
                metavar = " ".join(map(str, subaction.metavar))
                # need some changes in template file
            else:
                metavar = subaction.dest
            if action.help and action.help != SUPPRESS_HELP:
                helpstr = str(subaction.help).replace("'", "'\\''")
            else:
                helpstr = ""
            command = "'" + metavar + ":" + helpstr + "'"
            commands += [command]
            subactions = action._name_parser_map[subaction.dest]._actions
            subflags = []
            nargs_is_plus = False
            for subaction in subactions:
                subflag = generate_flag(subaction)
                subflags += [subflag]
                if subaction.dest in ["xcolumn", "ycolumn", "lines"]:
                    nargs_is_plus = True
            if nargs_is_plus:
                subflags += ["'*:int'"]
            case = case_template.replace("{{metavar}}", metavar)
            case = case.replace("{{flags}}", " \\\n          ".join(subflags))
            cases += [case]

with open(ZSH_COMPLETION_TEMPLATE) as f:
    template = f.read()

template = template.replace("{{programs}}", " ".join(BINNAMES))
template = template.replace("{{flags}}", " \\\n  ".join(flags))

template = template.replace("{{program}}", BINNAME)
template = template.replace("{{subparser}}", subparser)
template = template.replace("{{commands}}", "\n      ".join(commands))
template = template.replace("{{cases}}", "\n".join(cases))

with (
    open(ZSH_COMPLETION_FILE, "w")
    if ZSH_COMPLETION_FILE != "-"
    else sys.stdout
) as f:
    f.write(template)
