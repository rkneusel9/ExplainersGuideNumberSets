#  Harshad numbers.  Code given in A005349, modified
import sys

def harshad(N):
    return [n for n in range(1, N+1) if not n % sum([int(d) for d in str(n)])]

N = int(sys.argv[1])
x = []
y = []
k = 10000
while k<N:
    h = harshad(k)
    print("1..%8d: %0.10f" % (k, len(h)/k))
    x.append(k)
    y.append(len(h)/k)
    k += 10000

import matplotlib.pylab as plt
plt.plot(x,y,color='k')
plt.xlabel("$n$")
plt.ylabel("Fraction Harshad")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("harshad_numbers.png", dpi=300)
plt.show()

