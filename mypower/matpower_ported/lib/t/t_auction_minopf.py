def t_auction_minopf(*args,nout=1,oc=None):
	if oc == None:
		from ..oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.t_auction_minopf(*args,nout=nout)
