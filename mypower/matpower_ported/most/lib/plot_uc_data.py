def plot_uc_data(*args,nout=1,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.plot_uc_data(*args,nout=nout)
