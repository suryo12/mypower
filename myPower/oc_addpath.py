from oct2py import Oct2Py

def oc_addpath(path,oc=None):
    if oc == None:
        oc = Oct2Py()
    oc.addpath(path)
    return oc