def qps_mosek(*args,nout=5,oc=None):
	if oc == None:
		from ....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.qps_mosek(*args,nout=nout)