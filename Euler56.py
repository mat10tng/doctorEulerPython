from doctorNumber import *
max = 0
for i in range(2,100):
	for j in range(1,101):
		sm = sum(toArray(i**j))
		if sm > max:
			max = sm
print(max)