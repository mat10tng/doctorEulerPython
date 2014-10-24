from doctorPrime import *
lst = findPrimeBelow(1000000)
print(len(lst))
currentLength = 0
winner = 2
currentElement = 0 

while currentElement < 1000000/2:
	currentElement = lst.pop(0)
	sm = currentElement
	count = 1
	for x in range(len(lst)):
		sm+= lst[x]
		if sm < 1000000:
			count+= 1
			if isPrime(sm):
				if currentLength < count:
					currentLength = count
					winner = lst[x]
					print("this is winner", winner, count, sm)
		else:
			break

print (winner, currentLength)