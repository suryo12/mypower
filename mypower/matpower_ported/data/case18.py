def case18(*args,nout=1,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.case18(*args,nout=nout)
