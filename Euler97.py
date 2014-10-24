from doctorNumber import *
print( find_n_last_digits(123456789,10))
number = 2
R= 7830457
for i in range(R-1):
	number = find_n_last_digits(2*number,10)
	if(i%100000 == 0):
		print(i)
number = find_n_last_digits(28433*number+1,10)
print(number)