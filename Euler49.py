from doctorPrime import *
from doctorNumber import *
from itertools import *

prime_lst = findPrimeBelow(10000)
prime_lst = [prime for prime in prime_lst if prime > 999 and prime < 10000]

lst = list()
for element in prime_lst:
	lst_permutations = permutations(str(element))
	lst_permutations = [toNumber(element) for element in lst_permutations]
	lst_permutations = set([element for element in lst_permutations if element in prime_lst])
	prime_lst = [element for element in prime_lst if element not in lst_permutations]
	if len(lst_permutations)> 2 :
		lst.append(sorted(lst_permutations))

founded = False
for permutations in lst:
	for i  in range(len(permutations)):
		currentElement = permutations[i]
		for x in range(i+1,len(permutations)):
			distance = permutations[x] - currentElement
			if (permutations[x]+ distance) in permutations:
				print(permutations[i], permutations[x], permutations[x]+distance)
			if (permutations[x] + distance) > permutations[-1]:
				break;


			if founded:
				break;
		if founded:
			break;
	if founded:
		break;


print(lst)