# import
from mypower.api import pretty
from mypower.matpower_api import runpf
import mypower.api as myp

# runpf with default nout = max_nout from matpower_api
result = runpf()
print('runpf output: ',pretty(result))
print('runpf output type: ',type(result))

# runpf with default nout = 1 from api
oc = myp.oc_matpower()
result = oc.runpf()
print('runpf output: ',pretty(result))
print('runpf output type: ',type(result))