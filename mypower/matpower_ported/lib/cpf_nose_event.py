def cpf_nose_event(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.cpf_nose_event(*args,nout=nout)
