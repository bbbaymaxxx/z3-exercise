#!usr/bin/env python

from z3 import *

x = Int('x')
y = Int('y')

s = Solver()
s.add(x + y == 8)
s.add(2 * x - 3 * y == 6)

print(s.check())
print(s.model())
