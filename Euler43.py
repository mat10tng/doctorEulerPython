from itertools import *
from doctorNumber import *
number = "0123456789"
numbers = permutations(number)

lst = list()
for permutation in numbers:
	currentNumber = str(toNumber(permutation))
	count = 0
	for i in range(1,8):
		prime_lst = [2,3,5,7,11,13,17]
		if int(currentNumber[i:i+3]) % prime_lst[i-1] == 0:
			count+= 1
			if count > 6:
				lst.append(int(currentNumber))
		else:
			break

print(sum(lst))