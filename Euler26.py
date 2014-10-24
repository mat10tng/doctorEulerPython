from ReadFile import *
from decimal import *

maxLen = 0
maxD = 0 
for element in range(1,1000):
	lstRemainder = list()
	count = 0
	remainder = 1
	value = 1
	while remainder!= 0 and remainder not in lstRemainder:
		lstRemainder.append(value)
		value  = value*10
		remainder = value%element
		value = remainder
		if maxLen < len(lstRemainder):
			maxLen = len(lstRemainder)
			maxD = element
			print(maxD)

print(maxD)