from doctorPrime import *

limit = 10000
prime_lst = findPrimeBelow(limit)
odd_lst = list(range(3,limit,2))
odd_composite = find_odd_composite_under(limit)
square_lst = list(range(1,100))
square_lst = [element**2 for element in square_lst]
answer = False
print("hello")
for element in odd_composite:
	for prime in prime_lst:
		if prime > element:
			print (element)
			answer = True
			break
		if (element-prime)%2 == 0:
			temp = (element-prime)/2
			if temp in square_lst:
				break
	if answer:
		break