def compare_case(*args,nout=26,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.compare_case(*args,nout=nout)
