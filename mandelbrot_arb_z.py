#
#  file: mandelbrot.py
#
#  Generate a Mandelbrot set image
#
#  RTK, 06-Feb-2022
#  Last update:  06-Feb-2022
#
################################################################

import sys
import numpy as np
from matplotlib import cm
from PIL import Image


################################################################
#  Mandelbrot
#
def Mandelbrot(n, x0,x1,xinc, y0,y1,yinc, nmax, cname):
    """Generate a collection of Mandelbrot points and colors"""

    try:
        cmap = cm.get_cmap(cname)
    except:
        cmap = cm.get_cmap("inferno")
    
    X = []
    Y = []
    C = []

    x = x0
    i = 0
    while (x <= x1):
        y = y0
        j = 0
        while (y <= y1):
            c = complex(x,y)
            z = 0+0j
            for k in range(nmax):
                try:
                    z = z**n + c
                except:
                    z = c
                if (np.abs(z) > 2):
                    break
            X.append(i)
            Y.append(j)
            w = cmap(int(256*(k/nmax)))
            if (k == nmax-1):
                C.append((0,0,0))
            else:
                C.append((w[0],w[1],w[2]))
            y += yinc
            j += 1
        x += xinc
        i += 1

    return X,Y,C


################################################################
#  CreateOutputImage
#
def CreateOutputImage(X,Y,C):
    """Take the Mandelbrot points and create the output image"""

    x = np.array(X)
    y = np.array(Y)
    xmin = x.min(); xmax = x.max()
    dx = xmax - xmin
    ymin = y.min(); ymax = y.max()
    dy = ymax - ymin
    img = np.zeros((dy,dx,3), dtype="uint8")
    
    for i in range(len(x)):
        xx = int((dx-1)*(x[i] - xmin) / dx)
        yy = int((dy-1)*(y[i] - ymin) / dy)
        c = C[i]
        img[ymax-yy-1,xx,0] = int(255*c[0])
        img[ymax-yy-1,xx,1] = int(255*c[1])
        img[ymax-yy-1,xx,2] = int(255*c[2])

    return img


if (len(sys.argv) == 1):
    print()
    print("mandelbrot <z> <x0> <x1> <xinc> <y0> <y1> <yinc> <n> <cmap> <output>")
    print()
    print("  <z>          - exponent on z")
    print("  <x0,x1,xinc> - low, high, inc in x")
    print("  <y0,y1,yinc> - low, high, inc in y")
    print("  <n>          - max iterations per point")
    print("  <cname>      - color map name")
    print("  <output>     - output image name")
    print()
    exit(0)

n    = eval(sys.argv[1])

x0   = float(sys.argv[2])
x1   = float(sys.argv[3])
xinc = float(sys.argv[4])

y0   = float(sys.argv[5])
y1   = float(sys.argv[6])
yinc = float(sys.argv[7])

nmax = int(sys.argv[8])

cname = sys.argv[9]
oname= sys.argv[10]

X,Y,C = Mandelbrot(n, x0,x1,xinc, y0,y1,yinc, nmax, cname)
Image.fromarray(CreateOutputImage(X,Y,C)).save(oname)

