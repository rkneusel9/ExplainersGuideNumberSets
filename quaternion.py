#
#  file:  quaternion.py
#
#  Rotations in 3D space using quaternions
#
#  convert -delay 10 -loop 0 frames/*.png animation.gif
#
#  RTK, 19-Feb-2022
#  Last update:  20-Feb-2022
#
################################################################

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from NumberSets import *

def PlotPoints(x,y,z,fname=None):
    """Plot the given set of points"""
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot(x,y,z, linewidth=0.3, marker='+', markersize=3, color='k')
    if (fname != None):
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.savefig(fname, dpi=100)
    plt.close()


def Rotate(x,y,z, angle, axis):
    """Rotate the collection of points about the given axis"""

    def RotatePoint(x,y,z, a,ax):
        """Rotate a single point"""
        s = ax*np.sin(a/2)
        h = Quaternion(np.cos(a/2), s[0],s[1],s[2])
        hs= Quaternion(np.cos(a/2), -s[0], -s[1], -s[2])
        p = Quaternion(0, x,y,z)
        z = h*p*hs
        return list(z)[1:]

    X = [];  Y = [];  Z = []
    for i in range(len(x)):
        a,b,c = RotatePoint(x[i],y[i],z[i], angle, axis)
        X.append(a)
        Y.append(b)
        Z.append(c)
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    return X,Y,Z

# an expanding spiral
t = np.linspace(0,100*np.pi,1000)
z = t/10
x = t*np.cos(t)
y = t*np.sin(t)

# rotate about given axis
axis = np.array([float(i) for i in sys.argv[1].split("x")])

for n,angle in enumerate(np.linspace(0, 2*np.pi, 360//3)):
    fname = "frames/frame_%03d.png" % n
    X,Y,Z = Rotate(x,y,z, angle, axis=axis)
    PlotPoints(X,Y,Z,fname)
    print("frame #%d" % n)

