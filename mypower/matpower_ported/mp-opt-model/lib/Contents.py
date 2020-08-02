def Contents(*args,nout=0,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.Contents(*args,nout=nout)
