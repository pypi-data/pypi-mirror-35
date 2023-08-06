from os import path
from . import version

try:
    __version__ = version.read(path.dirname(__file__))
except IOError:
    # VERSION file was not created yet
    __version__ = '0.dev0'
