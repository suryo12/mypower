def params_var(*args,nout=4,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.params_var(*args,nout=nout)
