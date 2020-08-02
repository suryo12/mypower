def describe_idx(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.describe_idx(*args,nout=nout)
