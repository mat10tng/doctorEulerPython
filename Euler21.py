
from doctorPrime import *
lstPrime=findPrimeBelow(10000)
sm = 0
lstNatural = list(range(1,10000))
for x in lstNatural:
	y = sum(findDivisor(x,lstPrime))
	if y < 10000:
		xTemp = sum(findDivisor(y,lstPrime))
		if (x == xTemp) and (x != y) and(y !=1):
			sm = sm + x + y
			lstNatural.remove(x)
			lstNatural.remove(y)

print("final answer")
print(sm)