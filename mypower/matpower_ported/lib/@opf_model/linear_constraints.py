def linear_constraints(*args,nout=3,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.linear_constraints(*args,nout=nout)
