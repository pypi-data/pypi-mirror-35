"""sci - design, execute and share any lab experiment they can dream up"""

__version__ = '0.1.0'
__author__ = 'scici <sci@sci.ci>'
__all__ = []

from ._units import units
import os
from pathlib import Path

def sci_path(filename: str=None):
    home = str(Path.home()) 
    if filename:
        return home + '/sci/' + filename
    else:
        return home + '/sci'