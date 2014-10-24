#check if the number is pandigital
def is_pandigital(number):
	number = list(str(number))
	for i in range(1,len(set(number))+1):
		if str(i) in number:
			number.remove(str(i))
		else:
			return False
	return len(number)== 0