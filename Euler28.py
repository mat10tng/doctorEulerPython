from doctorPrime import *
from sympy.ntheory import *
primeLst = findPrimeBelow(1000*1000 +1000 + 1000)
primeB = findPrimeBelow(1000)
pro= 0
maxCount = 0
for a in range(-999,1000):
	print(a)
	for b in primeB:
		n = 0
		while isprime(n*n + a*n + b):
			n+= 1
		if maxCount < n:
			maxCount = n
			pro = a*b

		n = 0
		while isprime(n*n + a*n + b*(-1)):
			n+= 1
		if maxCount < n:
			maxCount = n
			pro = a*b*(-1)

print(pro)