def idx_ct(*args,nout=28,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.idx_ct(*args,nout=nout)
