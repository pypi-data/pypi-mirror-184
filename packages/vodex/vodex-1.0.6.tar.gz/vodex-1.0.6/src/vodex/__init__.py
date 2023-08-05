"""Volumetric Data and Experiment manager.

Modules exported by this package:

- `loaders`: The classes to read the image data and metadate from files.
- `core`: The core classes to organise the information about the experiment.
- `dbmethods`: The classes to create, write to and query the data base.
- `utils`: Some helper functions.
"""
from .loaders import *
from .core import *
from .dbmethods import *
from .experiment import *

# Version of the vodex package
__version__ = "1.0.6"
