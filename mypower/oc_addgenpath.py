from oct2py import Oct2Py

def oc_addgenpath(path,oc=None):
    if oc == None:
        oc = Oct2Py()
    oc.addpath(oc.genpath(path))
    return oc