import sys
import os
try:
    import lib2to3
except ImportError:
    import pgen
    import lib2to3

path = [os.path.abspath('')]


# default to None indicates 'relative paths' so that as a self-contained
# archive, pyjs can run its tests.
try:
    import pyjswidgets
    import pyjswaddons
    pyjspth = os.path.abspath(os.path.join(__file__,'../'))
    path += [os.path.dirname(pyjswidgets.__file__),
             os.path.dirname(pyjswaddons.__file__), ]
except ImportError:
    pyjspth = None

if 'PYJSPATH' in os.environ:
    for p in os.environ['PYJSPATH'].split(os.pathsep):
        p = os.path.abspath(p)
        if os.path.isdir(p):
            path.append(p)

MOD_SUFFIX = '.js'

PYTHON = os.path.realpath(sys.executable) if sys.executable else None
if PYTHON is None or not os.access(PYTHON, os.X_OK):
    PYTHON = 'python'


