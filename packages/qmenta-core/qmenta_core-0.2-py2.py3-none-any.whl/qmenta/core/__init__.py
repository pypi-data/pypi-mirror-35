from os import path
from . import version

__version__ = version.create(
    release='0.2',
    revfile=path.join(path.dirname(__file__), 'REVISION')
)
