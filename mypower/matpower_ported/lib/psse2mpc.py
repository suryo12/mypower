def psse2mpc(*args,nout=2,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.psse2mpc(*args,nout=nout)
