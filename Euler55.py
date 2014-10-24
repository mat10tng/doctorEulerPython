from doctorNumber import *
R = 10000
count = 0
for i in range(1,10000):
	if is_Lychrel_number(i,50):
		count+=1
print(count)

