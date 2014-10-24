# if toList true, make every element to a list else, append the entire line as one element
def readFile(s,toList):
	f = open(s,'r')
	lst = list()
	for line in f:
		line = line.rstrip('\n').split()
		if toList:
			lst+= line
		else:
			lst.append(line)
	return lst


# if all element in the list has the same value
def all_same(values):
 	return values.count(values[0]) == len(values)