def mpoption_info_intlinprog(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.mpoption_info_intlinprog(*args,nout=nout)
