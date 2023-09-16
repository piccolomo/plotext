# added by user @Freed-Wu as a replacement for package shtab if not present and in particular its method add_argument_to

FILE = None
DIRECTORY = DIR = None

def add_argument_to(parser, *args, **kwargs):
    from argparse import Action
    Action.complete = None
    return parser
