from doctorTriangle import *

found = False
i = 0
while not found:
	i += 1
	triNumber = findTriNumber(i)
	if triNumber > 40755 and is_pentagon(triNumber) and is_hexagon(triNumber):
		print(triNumber)
		found = True