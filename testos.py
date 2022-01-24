#!/usr/bin/python3

import subprocess as sp

x = sp.getstatusoutput("date")

y = x[0]

z = x[1]


print(z)
print(y)
