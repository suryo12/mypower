def run_userfcn(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.run_userfcn(*args,nout=nout)
