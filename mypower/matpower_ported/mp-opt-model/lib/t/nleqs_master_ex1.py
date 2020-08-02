def nleqs_master_ex1(*args,nout=2,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.nleqs_master_ex1(*args,nout=nout)
