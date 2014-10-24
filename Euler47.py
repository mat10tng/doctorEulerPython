from doctorPrime import *


lst = findPrimeDivisorCountUnder(200000)
count = 0
number = 0
while count!= 4:
	element = lst.pop(0)
	number+=1
	if element == 4:
		count+= 1
	else:
		count = 0

print(number-3)
