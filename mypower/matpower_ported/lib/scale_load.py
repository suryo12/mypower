def scale_load(*args,nout=3,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.scale_load(*args,nout=nout)