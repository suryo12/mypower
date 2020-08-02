def test_everything_ex1(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.test_everything_ex1(*args,nout=nout)
