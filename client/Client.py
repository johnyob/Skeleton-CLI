"""
Skeleton Client

Usage:
  client hello world

Options:
  -h --help                      Show this screen.
  --version                      Show version.

Help:
  For help, please see https://github.com/johnyob/Skeleton-CLI
"""

from importlib import import_module
from functools import reduce
import json

from docopt import docopt

from client.helpers.Constants import COMMANDS_JSON
from client.helpers.Util import read_file
from client import __version__


class Client:

    def __init__(self):
        """
        Client Class.

        Retrieves options from docopt. Options are then filtered using data stored in commands.json.
        Command is then imported and instantiated.
        """

        self._options = docopt(__doc__, version=__version__)

        commands_json = json.loads(read_file(COMMANDS_JSON))
        command = list(filter(lambda x: self._is_command(x["Conditions"]), commands_json))[0]

        getattr(
            import_module("client.commands.{0}".format(command["Module Identifier"])),
            command["Class Identifier"]
        )(self._options).run()

    def _is_command(self, conditions):
        return reduce(lambda x, y: x and y, map(lambda y: self._options[y], conditions))
