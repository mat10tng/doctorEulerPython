from doctorPrime import *


sm = 0
count = 0
number = 5
while count != 11:
	prime = str(findPrime(number))
	isTrucatable = True
	for i in range(len(prime)):
		if (not isPrime(int(prime[i::])) ) or ( not isPrime(int(prime[:len(prime)-i:])) ):
			isTrucatable = False
	print(prime)
	number+= 1
	if isTrucatable:
		sm+= int(prime)
		count+= 1
		print(count)
print(sm)
