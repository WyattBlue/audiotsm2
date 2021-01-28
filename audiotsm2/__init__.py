'''__init__.py'''

import os
import sys

# Fix not being able to find other modules.
dirPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(dirPath))

from phasevocoder import phasevocoder