def runcpf(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.runcpf(*args,nout=nout)
