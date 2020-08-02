def printpf(*args,nout=9,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.printpf(*args,nout=nout)
