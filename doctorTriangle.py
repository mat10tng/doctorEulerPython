
#return the triangle numbers at pos
def findTriNumber(pos):
    return int(pos*(pos+1)/2)

 # find all triangle number under number 
def triangle_under(number):
	lst = list()
	currentNumber = 1
	currentNatural = 2
	while currentNumber < number:
		lst.append(currentNumber)
		currentNumber += currentNatural
		currentNatural+= 1
	return lst

# find all triable number to position (include the position)

def triangle_to(pos):
	lst = list()
	currentNumber = 1
	currentNatural = 2
	while currentNatural != pos+2:
		lst.append(currentNumber)
		currentNumber += currentNatural
		currentNatural+= 1
	# other cool implementation :
	#lst = list(range(1,10))
	#lst = [sum(lst[:element]) for element in lst]

	return lst

def is_pentagon(number):
	return ((24*number +1)**(0.5)+1)% 6 == 0

def is_hexagon(number):
	return ((8*number +1)**(0.5)+1)%4 == 0