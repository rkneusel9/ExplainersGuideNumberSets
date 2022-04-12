# examples with fractions, etc
import numpy as np
import sys
from fractions import *

N = int(sys.argv[1])

p = Fraction(np.pi)
pi = p
for i in range(N):
    p= p*p*p + 33*p*p + Fraction(1,1)
    p= p - Fraction(1,1)
    p= p - 33*pi**2
    p= p/(pi*pi)
pi = p

p = np.pi
for i in range(N):
    p= p*p*p + 33*p*p + 1
    p= p - 1
    p= p - 33*np.pi**2
    p= p/(np.pi*np.pi)
pf = p

print("pi       : %0.18f (%s)" % (np.pi, str(Fraction(np.pi))))
print("rational : %0.18f (%s)" % (float(pi), str(pi)))
print("computer : %0.18f (%s)" % (pf, str(Fraction(pf))))
print()

exit(0)

c2 = np.pi*np.pi
print("computer's pi^2            : %0.18f" % c2)
print("computer's pi^2 as rational: %s" % str(Fraction(c2)))
pi2 = Fraction(np.pi) * Fraction(np.pi)
print("rational pi^2              : %s" % str(pi2))
print()
d2 = Decimal(pi2.numerator) / Decimal(pi2.denominator)
print("rational pi^2 as decimal   : %s" % str(d2))
c2 = Fraction(c2)
f2 = Decimal(c2.numerator) / Decimal(c2.denominator)
print("computer's pi^2 as decimal : %s" % str(f2))

cp = "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550"
dpi = Decimal(cp)
dp2 = dpi*dpi
print("decimal pi^2 to 132 places : %s" % str(dp2))
print()


