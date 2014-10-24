from doctorNumber import *
from doctorPrime import *

sum = 0
for number in range(1,1000000):
	if isPalin(number) and isPalin(dec_to_bin(number)):
		sum+= number

print (sum)