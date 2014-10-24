from doctorNumber import *
from doctorPandigital import *
number = "123456789"
permutation = number_permutations(number,9)
lst = list()
founded = False
for p in permutation[::-1]:
	p = str(p)

	for x in range(1,7):
		num = int(p[:x])
		concatenatingNumber = str(num)
		i = 1
		while len(concatenatingNumber) < 9:
			i += 1
			nextNumber = str(num*i)
			nextConc =  p[len(concatenatingNumber):len(concatenatingNumber)+len(nextNumber)]
			if nextNumber != nextConc:
				break
			concatenatingNumber+= nextConc
			if concatenatingNumber == p:
				print(p,"hello")
				founded = True
				break
		if founded:
			break
	if founded:
		break

