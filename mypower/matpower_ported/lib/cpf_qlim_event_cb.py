def cpf_qlim_event_cb(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.cpf_qlim_event_cb(*args,nout=nout)
