from doctorTriangle import *

currentPairSmallest = 0

n = 2
pentagon_lst = list()
pentagon_lst.append(1)
while 1:
	currentNumber = n*(3*n -1) / 2
	currentDifferent = currentNumber -pentagon_lst[-1]
	pentagon_lst.append(currentNumber)
	for element in pentagon_lst[::-1]:
		if is_pentagon(currentNumber-element) and is_pentagon(currentNumber+element):
			currentPairSmallest = currentNumber-element
			print(currentPairSmallest)
			break
	n+=1