def d2AIbr_dV2(*args,nout=4,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.d2AIbr_dV2(*args,nout=nout)
