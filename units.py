#
#  file:  units.py
#
#  Search for integers solving the sum of N unit fractions == 1.
#
#  RTK, 17-Jan-2022
#  Last update:  21-Jan-2022
#
################################################################

import os
import sys
import numpy as np
from RO import *
from DE import *
from GA import *
from GWO import *
from Jaya import *
from PSO import *
from Bounds import *
from RandomInitializer import *
from LinearInertia import *
from fractions import *

class Objective:
    def Evaluate(self, p):
        ans = Fraction(0,1)
        for i in range(len(p)):
            ans = ans + Fraction(1,int(np.round(p[i])))
        return np.abs(float(Fraction(1,1) - ans))

def main():
    if (len(sys.argv) == 1):
        print()
        print("units.py <npart> <max> <alg> <N>")
        print()
        print("  <npart>  - number of particles")
        print("  <max>    - max iterations")
        print("  <alg>    - RO,PSO,JAYA,GWO,DE,GA")
        print("  <N>      - number of unit fractions")
        print()
        return

    npart = int(sys.argv[1])
    miter = int(sys.argv[2])
    alg = sys.argv[3].upper()
    N = int(sys.argv[4])

    #  [1,101] for initial population
    lower = [0.9]*N
    upper = [101]*N
    b = Bounds(lower, upper, enforce="resample")
    i = RandomInitializer(npart=npart, ndim=N, bounds=b)

    #  [1,400] for general population
    #upper = [400]*N
    b = Bounds(lower,upper,enforce="resample")
    obj = Objective()

    if (alg == "RO"):
        swarm = RO(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, tol=1e-8)
    elif (alg == "PSO"):
        swarm = PSO(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b,
                    inertia=LinearInertia(), bare=False, bare_prob=0.5, ring=False, neighbors=4, tol=1e-8)
    elif (alg == "JAYA"):
        swarm = Jaya(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, tol=1e-8)
    elif (alg == "GWO"):
        swarm = GWO(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, eta=2, tol=1e-8)
    elif (alg == "GWO4"):
        swarm = GWO(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, eta=4, tol=1e-8)
    elif (alg == "DE"):
        swarm = DE(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, tol=1e-8)
    elif (alg == "GA"):
        swarm = GA(obj=obj, npart=npart, ndim=N, max_iter=miter, init=i, bounds=b, tol=1e-8)
    else:
        raise ValueError("Unknown swarm algorithm: %s" % alg)

    swarm.Optimize()
    res = swarm.Results()
    p = np.round(res["gpos"][-1])
    p.sort()
    v = res["gbest"][-1]
    s = Fraction(0,1)
    w = ""
    for i in range(N-1):
        t = Fraction(1,int(p[i]))
        s = s + t
        w += ("%s + " % str(t))
    t = Fraction(1,int(p[-1]))
    s = s + t
    w += ("%s = %s  (%d)" % (str(t), str(s), res["iterations"]))
    print(w)

if (__name__ == "__main__"):
    main()

