def d2Imis_dVdSg(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.d2Imis_dVdSg(*args,nout=nout)
