def params_legacy_cost(*args,nout=4,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.params_legacy_cost(*args,nout=nout)
