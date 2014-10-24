from doctorPrime import *
current_number = 10**12
found = False
while not found:
	product = current_number*(current_number-1)/2
	blue_disks = int(product**(1.0/2))
	if blue_disks*(blue_disks+1) == product:
		found = true
		print(blue_disks+1)
	current_number+=1
