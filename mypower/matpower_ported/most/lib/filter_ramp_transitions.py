def filter_ramp_transitions(*args,nout=1,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.filter_ramp_transitions(*args,nout=nout)
