import sys
from decimal import *

getcontext().prec = 100

x = Decimal(1)
print("%8d: %s" % (0, str(Decimal(x))))

for i in range(int(sys.argv[1])):
    x = x / Decimal(2) + Decimal(1) / x
    print("%8d: %s" % (i+1, str(x)))
print("  Exact: ", Decimal(2).sqrt())
print()

