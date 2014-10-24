from doctorNumber import *
from ReadFile import *
limit = 100
for x in range(10,limit):
	for y in range(x+1,limit):
		xArray = toArray(x)
		yArray = toArray(y)
		common = list(set([element for element in xArray if element in yArray]))
		for i in range(len(common)):
			x_temp = list(xArray)
			x_temp.remove(common[i])
			y_temp = list(yArray)
			y_temp.remove(common[i])
			if y_temp[0] == 0 or (x%10 == 0 and y %10 == 0):
				pass
			elif x_temp[0]/y_temp[0] == x/y:
				print(x_temp[0],y_temp[0])