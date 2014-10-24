from doctorPrime import *
from doctorNumber import * 
prime_lst = set(findPrimeBelow(1000000))
count = 0
print(len(prime_lst))
num = 0
for element in prime_lst:
	num+= 1
	lst = toArray(element)
	cont = True
	for x in lst:
		if x % 2 == 0:
			cont = False
	if cont:
		temp = str(element)
		permutations = set()
		permutations.add(element)
		for i in range(len(temp)-1):
			temp = temp[1:] + temp[0]
			permutations.add(int(temp))
		if permutations.issubset(prime_lst):
			count+= 1
			print(element)

# 2 is not added to list :/
print(count+1)