#
#  file: series_sqrt_2.py
#
#  Use a series summation to estimate sqrt(2).
#
#  RTK, 28-Jan-2022
#  Last update:  28-Jan-2022
#
################################################################

import sys
from decimal import *
getcontext().prec = 100

N = int(sys.argv[1])

def fact(n):
    ans = 1
    while (n >= 1):
        ans *= n
        n -= 1
    return ans

def fact2(n):
    ans = 1
    while (n >= 2):
        ans *= n
        n -= 2
    return ans

ans = Decimal(0.0)
for k in range(N):
    ans += Decimal(fact2(2*k-1)) / Decimal(4**k*fact(k))

print("sqrt(2) is approximately", ans)
print("exact is                ", Decimal(2).sqrt())

