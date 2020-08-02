def scenarios_ACTIVSg2000(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.scenarios_ACTIVSg2000(*args,nout=nout)
