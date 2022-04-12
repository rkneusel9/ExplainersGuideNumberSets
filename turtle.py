#
#  file: turtle.py
#
#  Draw the expansions of different real numbers
#
#  RTK, 03-Feb-2022
#  Last update:  03-Feb-2022
#
################################################################

import numpy as np
import sys 
import matplotlib.pylab as plt
from decimal import *

def NextPoint(p, angle, u):
    x,y = p
    t = angle*(np.pi/180.0)
    dx,dy = u*np.cos(t), u*np.sin(t)
    return x+dx, y+dy

if (len(sys.argv) == 1):
    print()
    print("turtle <steps> <value> [<output>]")
    print()
    print("  <steps> - number of steps to take")
    print("  <value> - expression (1/7, pi, e, int==sqrt)")
    print()
    exit(0)

unit = 1
steps= int(sys.argv[1])
vstr = sys.argv[2]

if (vstr.find("/") != -1):
    getcontext().prec = steps
    n,d = [int(i) for i in vstr.split("/")]
    value = Decimal(n) / Decimal(d)
    value = "".join([str(c) for c in value.as_tuple()[1]])
    if (len(value) < steps):
        value += "0"*(steps-len(value))
elif (vstr == "pi"):
    value = open("pi_billion.txt").read()[:steps]
elif (vstr == "e"):
    getcontext().prec = steps + 1
    value = str(Decimal(1).exp())[2:]
else:
    getcontext().prec = steps + 1
    v = int(np.floor(np.sqrt(int(vstr))))
    value = str(Decimal(int(vstr)).sqrt() - Decimal(v))[2:]

angle = 90.0
p = np.zeros((steps+1,2))

for i in range(1, steps+1):
    angle = (angle + int(value[i-1])*36.0) % 360
    p[i] = NextPoint(p[i-1], angle, unit)

#  plot
fig, ax = plt.subplots()

#  proper aspect ratio
dx = p[:,0].max() - p[:,0].min()
dy = p[:,1].max() - p[:,1].min()
ratio = dy/dx
x_left, x_right = ax.get_xlim()
y_low, y_high = ax.get_ylim()
ax.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)

#  plot and save
plt.axis('off')
ax.plot(p[:,0], p[:,1], color='k', linewidth=0.5)
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
if (len(sys.argv) == 4):
    plt.savefig(sys.argv[3], dpi=300)
plt.show()



