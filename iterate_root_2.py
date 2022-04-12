import sys
from decimal import *

getcontext().prec = 100

a,b = 1,1
print("%8d: %s" % (0, str(Decimal(a)/Decimal(b))))

for i in range(int(sys.argv[1])):
    a,b = a+2*b, a+b
    print("%8d: %s" % (i+1, str(Decimal(a)/Decimal(b))))

print("  Exact: ", Decimal(2).sqrt())

print("a =", a)
print("b =", b)
print()

