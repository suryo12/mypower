def runopf_w_res(*args,nout=1,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.runopf_w_res(*args,nout=nout)
