'''mypower.api
Pseudo package for all core functions of myPower.
Example:
    # import function individually into namespace
    from mypower.api import oc_matpower
    oc = oc_matpower

    # import all function
    import mypower.api as myp
    oc = myp.oc_matpower
'''

from __future__ import absolute_import

from .get_index import get_index
from .makeB_kron import makeB_kron
from .makeB_kron_slope import makeB_kron_slope
from .makeB_kron_slope import kron2slope
from .load_pkl import load_pkl
from .losses_kron import losses_kron
from .losses_kron import losses_kron_detailed
from .losses_kron_slope import losses_kron_slope
from .losses_kron_slope import losses_kron_slope_detailed
from .oc_addpath import oc_addpath
from .oc_addgenpath import oc_addgenpath
from .oc_matpower import oc_matpower
from .port import port
from .pretty import pretty
from .save_str import save_str
from .save_pkl import save_pkl
from .str_in import str_in
from .to_mypc import to_mypc
from .to_mypc0 import to_mypc0