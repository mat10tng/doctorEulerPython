from doctorNumber import *
not_found = True

a = 125874
b = 251748
x = 1
print(sorted(toArray(x))==sorted(toArray(x*7)))
while not_found:
	current_array = sorted(toArray(x))
	keep_going = True
	for i in range(2,7):
		if sorted(toArray(x*i))!= current_array:
			break
		if i == 6:
			print("hello")
			print(x)
			not_found = False
	x+=1
	if(x%1000000 == 0):
		print(x)
