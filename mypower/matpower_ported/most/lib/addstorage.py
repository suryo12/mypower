def addstorage(*args,nout=4,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.addstorage(*args,nout=nout)
