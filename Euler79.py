from doctorNumber import *
end = False
count = 0
power = 1
number = 1
while not end:
	length = len(toArray(number**power))
	if length == power:
		count+=1
		print(number, power, count)
	if length > power:
		power+=1
		if number == 9:
			end = True
		number = 1
	number +=1

print(count)

