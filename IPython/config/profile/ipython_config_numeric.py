#-------------------------------------------------------------------------------
#  Copyright (C) 2008-2011  The IPython Development Team
#
#  Distributed under the terms of the BSD License.  The full license is in
#  the file COPYING, distributed as part of this software.
#-------------------------------------------------------------------------------
c = get_config()

# This can be used at any point in a config file to load a sub config
# and merge it into the current one.
load_subconfig('ipython_config.py')

lines = """
import numpy
import scipy
import numpy as np
import scipy as sp
"""

# You have to make sure that attributes that are containers already
# exist before using them.  Simple assigning a new list will override
# all previous values.
if hasattr(c.Global, 'exec_lines'):
    c.Global.exec_lines.append(lines)
else:
    c.Global.exec_lines = [lines]
