def idx_cost(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.idx_cost(*args,nout=nout)
