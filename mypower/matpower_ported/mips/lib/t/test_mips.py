def test_mips(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_matpower import oc_matpower
	oc = oc_matpower()
	return oc.test_mips(*args,nout=nout)