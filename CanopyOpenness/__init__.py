#!/usr/bin/env/python
"""
Calculating canopy openness from photos program
"""
__version__ = "0.0.2"


import sys
from loguru import logger
from CanopyOpenness import CanOpen
from CanopyOpenness import ImageLoad


def set_loglevel(loglevel="INFO"):
    """
    Set the loglevel for loguru logger. Using 'enable' here as 
    described in the loguru docs for logging inside of a library.
    This sets the level at which logger calls will be displayed 
    throughout the rest of the code.

    Example:
      # example notebook usage:
      import CanopyOpenness
      CanopyOpenness.set_loglevel("DEBUG")
      ...

      # example statements written inside your code:
      from loguru import logger
      ...
      logger.debug("starting a new analysis")
      ...
    """
    config = {}
    config["handlers"] = [{
        "sink": sys.stdout,  # or sys.stderr, or a filename, ...
        "format": "{time:hh:mm} | {level: <7} | <b><magenta>{function: <15}</magenta></b> | <level>{message}</level>",
        "level": loglevel,
        "colorize": True, # sys.stdout.isatty() will only use color when supported.
    }]
    logger.configure(**config)
    logger.enable("CanopyOpenness")
