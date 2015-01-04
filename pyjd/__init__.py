import sys
import os

import pyjswidgets
import pyjswaddons
sys.path += [os.path.dirname(pyjswidgets.__file__),
             os.path.dirname(pyjswaddons.__file__), ]
from pyjs.runners import RunnerManager

#TODO: very ugly to self-import and setattr(self) ... remove ASAP!
import pyjd


pyjdversion = '0.9'


_manager = RunnerManager()
_manager.set_conf()
for key, value in _manager._conf.iteritems():
    setattr(pyjd, key, value)
_manager.set_runner()


#TODO: perm delete ASAP unless someone claims use; disable for now
sys.path += [os.path.dirname(__file__)]


add_setup_callback = _manager.add_setup_listener
setup = _manager.setup
run = _manager.run
