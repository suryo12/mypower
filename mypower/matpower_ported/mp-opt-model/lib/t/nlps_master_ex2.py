def nlps_master_ex2(*args,nout=2,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.nlps_master_ex2(*args,nout=nout)
