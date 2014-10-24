from ReadFile import *
from doctorTriangle import *
from doctorString import *
name_lst = readFile("Euler42Data.txt",True)
name_lst = name_lst[0].split(',')
name_lst = [element[1:-1].lower() for element in name_lst]
triangle_lst = triangle_under(1000)
count = 0

for name in name_lst:
	value = word_value(name)
	if value in triangle_lst:
		count+=1

print (count)