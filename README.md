# Skeleton Command Line Interface

> A simple modular command line interface skeleton program

This is an easy-to-use Python Command Line Interface (CLI) package that creates command endpoints based of a JSON file. 
The purpose of this package is that you should be able to use this as a template for building new CLI programs.
You can fork this project and customize it to your liking, or just use it as a reference.

##Features

### Client Interface
- [x] Create new commands by modifying the Client's docstring and `commands.json`
- [x] Identify commands based of system command line arguments using functional programming techniques and `commands.json`
- [x] Execute commands once Client identifies the command `Module Identifier` and `Class Identifier`

### Command Entity
- [x] Constructor 
- [x] Run method

### Utilities
- [x] Read files
- [x] Write to files

##Usage

### Adding new commands 

To add a new command to the Skeleton CLI package. 3 simple steps must be carried out. 
Firstly the docstring for the `docopt` parser must be modified. Having modified the docstring, the commands.json file must
be modified using the describe object structure (See below), and finally the command class for the new command must be implemented.

#### Docopt Docstrings

The Skeleton CLI package makes use of the [docopt](http://docopt.org/) Python package. Docopt is extremely useful as it 
provides a simple way of defining the interface for a command-line program and then automatically generates a
arguments parser for that program. 

To define the interface for a command-line program, docopt makes use of Python's PEP 257 docstrings conventions. An example docstring might be:
```python
"""
Usage:
  client file open <file>
  client file system list <path>
  client file system move <file> <to>
  client file system remove <file>
  
Options:
  -h, --help                     Show this screen.
  --version                      Show version.
 
Help:
  For help, see https://example.com/help
"""
```

Docopt then uses the docstring to produce a custom arguments parser which returns a dictionary with options and commands as keys. 
For example, if you invoke the command
```shell
client file open test.txt
```

the returned dictionary will be:
```python
{
  '<file>': 'test.txt',
  '<path>': None,
  '<to>': None,
  'file': True,
  'list': False,
  'move': False,
  'open': True,
  'remove': False,
  'system': False
}
```

#### JSON command structure

The JSON command structure:
- `Module Identifier`: Contains the string for the `import_module` path of the file containing the class that contains the run method for the command.
- `Class Identifier`: Contains the string for the identifier of the class that contains the run method for the command
- `Conditions`: Contains the list of string keys. These string keys reference the keys in the dictionary returned from `docopt`. The keys must only reference key, value pairs where the value is a boolean value. 

For example, for the command `client file open <file>`:

```json
{
  "Module Identifier": "file.Open",
  "Class Identifier": "Open",
  "Conditions": [
    "file",
    "open"
  ]
}
```

#### Command Class

Command Classes in the Skeleton CLI package make use of the `Command` base class. The `Command` base class contains a constructor which initializes the `_options` property. The `_options` property contains the dictionary returned from `docopt`. 
The `Command` base class also contains a `run` method, which is an abstract class method and therefore must be implemented in the subclasses. 


For example, for the command `client file open <file>`:
```python
from client.commands.Command import Command
from client.helpers.Util import read_file


class Open(Command):

    def __init__(self, options):
        super().__init__(options)
        self._file = self._options["<file>"]
        
    def run(self):
        file = read_file(self._file)
        
        print("\nFile ({0})".format(self._file))
        print(file)
```

## Errors
If you discover an error within this package, please email [me](mailto:alistair.o'brien@ellesmere.com).

## Credits
- [Alistair O'Brien](https://github.com/johnyob)