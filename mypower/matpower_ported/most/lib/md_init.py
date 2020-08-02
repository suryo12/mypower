def md_init(*args,nout=1,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.md_init(*args,nout=nout)
