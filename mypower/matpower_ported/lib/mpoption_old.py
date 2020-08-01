def mpoption_old(*args,nout=2,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.mpoption_old(*args,nout=nout)
