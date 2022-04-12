#
#  file:  pi_code.py
#
#  Search for stuff in the decimal expansion of pi
#
#  RTK, 25-Jan-2022
#  Last update:  27-Jan-2022
#
################################################################

import sys
import numpy as np

if (len(sys.argv) == 1):
    print()
    print("pi_code <string|number|hex|hs|letter> <target> [<target> ...]")
    print()
    print("  string|number - constant, interpret targets as string or number")
    print("  hex           - constant, use bytes version")
    print("  hs            - constant, string as hex")
    print("  letter        - constant, search for uppercase letters as digits 00..25")
    print("  <target>      - target string")
    print()
    exit(0)

if (sys.argv[1].lower() == "hex"):
    digits = open("pi_billion_16.txt").read()
    for target in sys.argv[2:]:
        pos = digits.find(target.upper())
        if (pos == -1):
            print("%s not found" % target)
        else:
            print("%s found starting at position %d, " % (target, pos), end="")
            lo = max(pos-15,0)
            hi = min(pos+len(target)+15,len(digits)-1)
            print("...%s %s %s..." % (digits[lo:pos], digits[pos:len(target)+pos], digits[(pos+len(target)):hi]))
elif (sys.argv[1].lower() == "hs"):
    digits = open("pi_billion_16.txt").read()
    for t in sys.argv[2:]:
        target = ""
        for c in t:
            target += "%02X" % ord(c)
        pos = digits.find(target.upper())
        if (pos == -1):
            print("[%s] %s not found" % (t, target))
        else:
            print("[%s] %s found starting at position %d, " % (t, target, pos), end="")
            lo = max(pos-15,0)
            hi = min(pos+len(target)+15,len(digits)-1)
            print("...%s %s %s..." % (digits[lo:pos], digits[pos:len(target)+pos], digits[(pos+len(target)):hi]))
elif (sys.argv[1].lower() == "letters"):
    digits = open("pi_billion.txt").read()
    for target in sys.argv[2:]:
        t = ""
        for c in target:
            t += "%02d" % (ord(c)-65)
        st = target
        target = t
        pos = digits.find(target)
        if (pos == -1):
            print("[%s] %s not found" % (st, target))
        else:
            print("[%s] %s found starting at position %d, " % (st, target, pos), end="")
            lo = max(pos-15,0)
            hi = min(pos+len(target)+15,len(digits)-1)
            print("...%s %s %s..." % (digits[lo:pos], digits[pos:len(target)+pos], digits[(pos+len(target)):hi]))

else:
    digits = open("pi_billion.txt").read()
    for target in sys.argv[2:]:
        st = ""
        if (sys.argv[1].lower() == "string"):
            t = ""
            for c in target:
                t += str(ord(c))
            st = target
            target = t
        pos = digits.find(target)
        if (pos == -1):
            if (st == ""):
                print("%s not found" % target)
            else:
                print("[%s] %s not found" % (st,target))
        else:
            if (st == ""):
                print("%s found starting at position %d, " % (target, pos), end="")
            else:
                print("[%s] %s found starting at position %d, " % (st, target, pos), end="")
            lo = max(pos-15,0)
            hi = min(pos+len(target)+15,len(digits)-1)
            print("...%s %s %s..." % (digits[lo:pos], digits[pos:len(target)+pos], digits[(pos+len(target)):hi]))

