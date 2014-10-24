from itertools import *

def isPalin(number):
	return number == int(str(number)[::-1])
def reverse_number(number):
	return int(str(number)[::-1])
def dec_to_bin(number):
	return int(bin(number)[2:])
def toArray(number):
	return list(map(int,str(number)))
def toSet(number):
	return set(map(int,str(number)))
def toNumber(arrayNumber):
	return int(''.join(map(str,arrayNumber)))
def number_permutations(number,i):
	permutation =permutations(toArray(number),i)
	permutation = [toNumber(element) for element in permutation]
	return permutation
def is_Lychrel_number(number, iteration):
	for i in range(iteration):
		number = number+ reverse_number(number)
		if isPalin(number):
s			return False
	return True
#give a number, save n last digits
def find_n_last_digits(number,n):
	lst = toArray(number)
	return toNumber(lst[-n:])

def find_next_chain_number(number):
	square_sum = toArray(number)
	square_sum = [i**2 for i in square_sum]
	number = sum(square_sum)
	return number