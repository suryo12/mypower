def find_islands(*args,nout=2,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.find_islands(*args,nout=nout)
