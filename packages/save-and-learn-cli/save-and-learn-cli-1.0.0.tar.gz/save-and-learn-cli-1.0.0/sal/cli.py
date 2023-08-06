"""
sal

Usage:
  sal bp
  sal -h | --help
  sal --version

Options:
  -h --help     Show help
  --version     Show version

Examples :
  sal bp

Help:
  For help using this tool, please open an issue on the GitHub repository :
  https://github.com/damienld22/save-and-learn
"""

from inspect import getmembers, isclass
from docopt import docopt

from . import __version__ as VERSION

def main():
  """Main CLI entrypoint."""
  import commands
  options = docopt(__doc__, version=VERSION)

  for k, v in options.iteritems():
    if hasattr(commands, k):
      module = getattr(commands, k)
      commands = getmembers(module, isclass)
      command = [command[1] for command in command if command[0] != 'Base'][0]
      command = command(options)
      command.run()