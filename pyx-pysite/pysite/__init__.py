"""
Pysite is a Python web framework, inspired by JSX. It uses Flask in the backend.
Common commands for the `pysite` CLI are `new <projectname>` and `run`.
"""

import js2py
import inspect
from . import tags
from typing import Callable
from flask import Flask

__version__ = "1.0.0"
