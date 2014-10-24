from doctorNumber import *
from doctorPrime import *

number = "123456789"
lst = list()
found = False
for i in range(9,1,-1):
	currentNumber = number[:i]
	permutation =list(permutations(currentNumber,i))
	permutation = [toNumber(element) for element in permutation]
	permutation = list(sorted(permutation))
	print(i, len(permutation))
	for element in permutation[::-1]:
		if isPrime(int(element)):
			print(element)
			found = True
			break
	if found:
		break