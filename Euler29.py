from sympy import *
from doctorPrime import *

lst = set()
for a in range(2,101):
	for b in range(2,101):
		if a**b not in lst:
			lst.add(a**b)

print(len(lst))
