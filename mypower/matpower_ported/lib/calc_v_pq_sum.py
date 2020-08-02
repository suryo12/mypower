def calc_v_pq_sum(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.calc_v_pq_sum(*args,nout=nout)
