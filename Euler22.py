from ReadFile import *
lst = readFile("Euler22Data.txt",True)
lst = lst[0].split(',')
lst = [element[1:-1] for element in lst]
lst.sort()

total = 0
for i in range(len(lst)):
	sm = 0
	for char in lst[i].lower():
		sm+= char_position(char)+1
	total += sm*(i+1)
print (total)