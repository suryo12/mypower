import os
def get_index(path_lib=None):
    '''myPower index based on MATPOWER'''
    if path_lib == None:
        path_lib=os.path.join(os.getcwd(),'matpower\\lib')

    idx = {
        # BUS
        # define bus types
        'PQ':'',      
        'PV':'',      
        'REF':'',     
        'NONE':'',    

        # define the indices
        'BUS_I':'',           # bus number (1 to 29997)
        'BUS_TYPE':'',        # bus type (1 - PQ bus, 2 - PV bus, 3 - reference bus, 4 - isolated bus)
        'PD':'',              # Pd, real power demand (MW)
        'QD':'',              # Qd, reactive power demand (MVAr)
        'GS':'',              # Gs, shunt conductance (MW at V = 1.0 p.u.)
        'BS':'',              # Bs, shunt susceptance (MVAr at V = 1.0 p.u.)
        'BUS_AREA':'',        # area number, 1-100
        'VM':'',              # Vm, voltage magnitude (p.u.)
        'VA':'',              # Va, voltage angle (degrees)
        'BASE_KV':'',         # baseKV, base voltage (kV)
        'ZONE':'',            # zone, loss zone (1-999)
        'VMAX':'',            # maxVm, maximum voltage magnitude (p.u.)      (not in PTI format)
        'VMIN':'',            # minVm, minimum voltage magnitude (p.u.)      (not in PTI format)

        # BRANCH
        # define the indices
        'F_BUS':'',           # f, from bus number
        'T_BUS':'',           # t, to bus number
        'BR_R':'',            # r, resistance (p.u.)
        'BR_X':'',            # x, reactance (p.u.)
        'BR_B':'',            # b, total line charging susceptance (p.u.)
        'RATE_A':'',          # rateA, MVA rating A (long term rating)
        'RATE_B':'',          # rateB, MVA rating B (short term rating)
        'RATE_C':'',          # rateC, MVA rating C (emergency rating)
        'TAP':'',             # ratio, transformer off nominal turns ratio
        'SHIFT':'',           # angle, transformer phase shift angle (degrees)
        'BR_STATUS':'',       # initial branch status, 1 - in service, 0 - out of service
        'ANGMIN':'',          # minimum angle difference, angle(Vf) - angle(Vt) (degrees)
        'ANGMAX':'',          # maximum angle difference, angle(Vf) - angle(Vt) (degrees)

        # included in power flow solution, not necessarily in input
        'PF':'',              # real power injected at "from" bus end (MW)       (not in PTI format)
        'QF':'',              # reactive power injected at "from" bus end (MVAr) (not in PTI format)
        'PT':'',              # real power injected at "to" bus end (MW)         (not in PTI format)
        'QT':'',              # reactive power injected at "to" bus end (MVAr)   (not in PTI format)

        # included in opf solution, not necessarily in input
        # assume objective function has units, u
        'MU_SF':'',         # Kuhn-Tucker multiplier on MVA limit at "from" bus (u/MVA)
        'MU_ST':'',         # Kuhn-Tucker multiplier on MVA limit at "to" bus (u/MVA)
        'MU_ANGMIN':'',     # Kuhn-Tucker multiplier lower angle difference limit (u/degree)
        'MU_ANGMAX':'',     # Kuhn-Tucker multiplier upper angle difference limit (u/degree)

        # COST
        # define cost models
        'PW_LINEAR':'',   
        'POLYNOMIAL':'',  

        # define the indices
        'MODEL':'',         # cost model, 1 = piecewise linear, 2 = polynomial 
        'STARTUP':'',       # startup cost in US dollars
        'SHUTDOWN':'',      # shutdown cost in US dollars
        'NCOST':'',         # number N = n+1 of end/breakpoints in piecewise linear
                            # cost function, or of coefficients in polynomial cost fcn
        'COST':'',          # parameters defining total cost function begin in this col
                            # (MODEL = 1) : p1, f1, p2, f2, ..., pN, fN
                            #      where p1 < p2 < ... < pN and the cost f(p) is defined
                            #      by the coordinates (p1,f1), (p2,f2), ..., (pN,fN) of
                            #      the end/break-points of the piecewise linear cost
                            # (MODEL = 2) : cn, ..., c1, c0
                            #      N coefficients of an n-th order polynomial cost fcn,
                            #      starting with highest order, where cost is
                            #      f(p) = cn*p^n + ... + c1*p + c0

        # GEN
        # define the indices
        'GEN_BUS':'',       # bus number
        'PG':'',            # Pg, real power output (MW)
        'QG':'',            # Qg, reactive power output (MVAr)
        'QMAX':'',          # Qmax, maximum reactive power output at Pmin (MVAr)
        'QMIN':'',          # Qmin, minimum reactive power output at Pmin (MVAr)
        'VG':'',            # Vg, voltage magnitude setpoint (p.u.)
        'MBASE':'',         # mBase, total MVA base of this machine, defaults to baseMVA
        'GEN_STATUS':'',    # status, 1 - machine in service, 0 - machine out of service
        'PMAX':'',          # Pmax, maximum real power output (MW)
        'PMIN':'',          # Pmin, minimum real power output (MW)
        'PC1':'',           # Pc1, lower real power output of PQ capability curve (MW)
        'PC2':'',           # Pc2, upper real power output of PQ capability curve (MW)
        'QC1MIN':'',        # Qc1min, minimum reactive power output at Pc1 (MVAr)
        'QC1MAX':'',        # Qc1max, maximum reactive power output at Pc1 (MVAr)
        'QC2MIN':'',        # Qc2min, minimum reactive power output at Pc2 (MVAr)
        'QC2MAX':'',        # Qc2max, maximum reactive power output at Pc2 (MVAr)
        'RAMP_AGC':'',      # ramp rate for load following/AGC (MW/min)
        'RAMP_10':'',       # ramp rate for 10 minute reserves (MW)
        'RAMP_30':'',       # ramp rate for 30 minute reserves (MW)
        'RAMP_Q':'',        # ramp rate for reactive power (2 sec timescale) (MVAr/min)
        'APF':'',           # area participation factor

        # included in opf solution, not necessarily in input
        # assume objective function has units, u
        'MU_PMAX':'',       # Kuhn-Tucker multiplier on upper Pg limit (u/MW)
        'MU_PMIN':'',       # Kuhn-Tucker multiplier on lower Pg limit (u/MW)
        'MU_QMAX':'',       # Kuhn-Tucker multiplier on upper Qg limit (u/MVAr)
        'MU_QMIN':'',       # Kuhn-Tucker multiplier on lower Qg limit (u/MVAr)

        # Note: When a generator's PQ capability curve is not simply a box and the
        # upper Qg limit is binding, the multiplier on this constraint is split into
        # it's P and Q components and combined with the appropriate MU_Pxxx and
        # MU_Qxxx values. Likewise for the lower Q limits.
    }

    with open(os.path.join(path_lib,'idx_bus.m'),'r') as txt:
        for line in txt:
            words = line.split()
            if len(words)>0:
                if words[0] in idx:
                    idx[words[0]] = int(words[2][:-1])

    with open(os.path.join(path_lib,'idx_brch.m'),'r') as txt:
        for line in txt:
            words = line.split()
            if len(words)>0:
                if words[0] in idx:
                    idx[words[0]] = int(words[2][:-1])
    
    with open(os.path.join(path_lib,'idx_cost.m'),'r') as txt:
        for line in txt:
            words = line.split()
            if len(words)>0:
                if words[0] in idx:
                    idx[words[0]] = int(words[2][:-1])
    
    with open(os.path.join(path_lib,'idx_gen.m'),'r') as txt:
        for line in txt:
            words = line.split()
            if len(words)>0:
                if words[0] in idx:
                    idx[words[0]] = int(words[2][:-1])

    return idx
if __name__ == '__main__':
    from myp_pretty import myp_pretty
    print(myp_pretty(get_index()))