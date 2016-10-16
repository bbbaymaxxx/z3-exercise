#!usr/bin/env python

from z3 import *

a = Real('a')
b = Real('b')
c = Real('c')
d = Real('d')


s = Solver()
s.add(2 * a + 5 * b + 3 * c + 3 * d == 1)
s.add(5 * a + 7 * b + 7 * c == 0)
s.add(3 * a + 7 * b + 6 * c + 9 * d == 0)
s.add(3 * a + 9 * c + 4 * d  == 0)

print(s.check())
print(s.model())

