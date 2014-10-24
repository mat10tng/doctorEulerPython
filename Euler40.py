from doctorNumber import *
count = 0
number = 1
prd = 1
tabl = [1,10,100,1000,10000,100000,1000000]
while count < 1000001:
	lst = toArray(number)
	for element in lst:
		count+=1
		if  count in tabl:
			prd*= element
	number += 1

print(prd)