#
#  file:  dual_test.py
#
#  Generate f(x) and f'(x)
#
#  RTK, 16-Feb-2022
#  Last update:  16-Feb-2022
#
################################################################

from dual import *
import matplotlib.pylab as plt

N = 200
dx = 20/N
x = [-10+i*dx for i in range(N+1)]
y = []
yp= []

for t in x:
    u = Dual(t,1)
    v = u*u.sin() + u*u.cos()
    y.append(v.a)
    yp.append(v.b)

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_1.png", dpi=300)
plt.show()

N = 200
dx = 10/N
x = [-5+i*dx for i in range(N+1)]
y = []
yp= []
a = []

for t in x:
    u = Dual(t,1)
    v = (Dual(-0.5,0)*u**2).exp()
    y.append(v.a)
    yp.append(v.b)

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_2.png", dpi=300)
plt.show()

N = 200
dx = 20/N
x = [-10+i*dx for i in range(N+1)]
y = []
yp= []
a = []

for t in x:
    u = Dual(t,1)
    v = (Dual(1,0) + (Dual(-1,0)*u).exp())**(-1)
    y.append(v.a)
    yp.append(v.b)

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_3.png", dpi=300)
plt.show()

# p[0]*np.sin(p[1]*x)+p[2]*np.exp(-0.5*(x-p[3])**2/p[4])
# 0:    1.9999757147829731
# 1:    3.0000012322708156
# 2:   19.9999999999999964
# 3:    7.9999997225274768
# 4:    0.6000182383275868

N = 200
dx = 10/N
x = [i*dx for i in range(N+1)]
y = []
yp= []
a = []

for t in x:
    u = Dual(t,1)
    v = Dual(2,0)*(Dual(3,0)*u).sin() + Dual(20,0)*(Dual(-0.5,0)*(u-Dual(8,0))**2/Dual(0.6,0)).exp()
    y.append(v.a)
    yp.append(v.b)

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_4.png", dpi=300)
plt.show()

N = 200
dx = 10/N
x = [0.0001+i*dx for i in range(N+1)]
y = []
yp= []
a = []

for t in x:
    u = Dual(t,1)
    v = u**2*(Dual(-1,0)*u).exp()
    y.append(v.a)
    yp.append(v.b)

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_5.png", dpi=300)
plt.show()

