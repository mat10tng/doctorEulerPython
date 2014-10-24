
from itertools import *
from sympy import *
from doctorNumber import *
factorial_lst = list()
limit = 10
normal_lst = list(range(0,limit))
for n in range(0,limit):
	factorial_lst.append(factorial(n))

count = 0
 # print(factorial(9)*7) 2540161
limit = 2540161
for i in range(9,limit):
	lst = toArray(i)
	sm = 0
	for element in lst:
		sm+= factorial_lst[element]
	if sm == i:
		count+= sm
		print(sm)
print (count)