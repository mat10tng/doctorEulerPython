from doctorPrime import *
from itertools import *
lstPrime = findPrimeBelow(30000)
lstAbundant = list()

for i in range(1,28123):
	if(i < sum(findDivisor(i,lstPrime))):
		lstAbundant.append(i)


lstAbundant = list(combinations_with_replacement(lstAbundant, 2))

lstAbundant = [reduce(lambda a,b:a+b,element) for element in lstAbundant]

lstAbundant = list(set(lstAbundant))

lstAbundant = [0 for element in lstAbundant if element < 28123]

sm = sum(range(0,28123)) - sum(lstAbundant)

