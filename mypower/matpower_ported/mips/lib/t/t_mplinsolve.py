def t_mplinsolve(*args,nout=2,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.t_mplinsolve(*args,nout=nout)
