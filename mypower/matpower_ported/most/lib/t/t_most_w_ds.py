def t_most_w_ds(*args,nout=4,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.t_most_w_ds(*args,nout=nout)
