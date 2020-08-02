def ex_load_profile(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.ex_load_profile(*args,nout=nout)
