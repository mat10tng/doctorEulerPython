from itertools import *
from functools import *

def gcd(a, b):
    while b!= 0:
        t = b
        b = a % b
        a = t
    return a

from sympy import *
#return a list of prime below z
def findPrimeBelow(z):
    naturalLst = list(range(1,z))   
    p = 2
    while p**2 < z:
        naturalLst[p+p-1::p] = [0]*len(naturalLst[p+p-1::p])
        p+= 1

        while (naturalLst[p-1]== 0 ):
            p+= 1
    naturalLst = [item for item in naturalLst if item > 1]
    return naturalLst

#Return a list of divisor with the provided prime list
def findDivisor(number, lstPrime):
    currentPrime = 0
    smallestNumber  = number
    lstPrimeCurrent = list()
    lstDivisor = list()
    if number in lstPrime:
        return [1]
    while currentPrime < smallestNumber :
        for prime in lstPrime:
            temp = number
            currentPrime = prime
            while temp % prime == 0:
                lstPrimeCurrent.append(prime)
                temp = int(temp/prime)
                if smallestNumber > temp :
                    smallestNumber = temp
                if prime not in lstDivisor:
                    lstDivisor.append(prime)
    divisor = 1
    lstDivisor.append(divisor)
    for i in range(2,len(lstPrimeCurrent)):
        lst = list(combinations(lstPrimeCurrent,i))
        for element in lst:
            divisor = reduce(lambda a,b:a*b,element)
            if divisor not in lstDivisor:
                lstDivisor.append(divisor)
    return lstDivisor

def findPrimeDivisor(number,prime_lst):
    st = set()
    while number!= 1:
        for prime in prime_lst:
            while number%prime == 0:
                number = number/prime
                st.add(prime)
    return st

def disectNumber(number,prime_lst):
    st = []
    while number!= 1:
        for prime in prime_lst:
            while number%prime == 0:
                number = number/prime
                st.append(prime)
    return st
def findPrimeDivisorCountUnder(z):
    naturalLst = list(range(1,z))
    divisor_lst =[0]*(z-1)
    p = 2
    while p*2 < z:
        for x in range(p+p-1,len(divisor_lst),p):
            naturalLst[x] = 0
            divisor_lst[x]+=1
        p+= 1
        while (naturalLst[p-1]== 0 ):
            p+= 1

    return divisor_lst
def find_odd_composite_under(z):
    naturalLst = list(range(1,z))
    divisor_lst = list(range(1,z))
    divisor_lst[:8]=[0]*9
    divisor_lst[4::2] = [0]*len(divisor_lst[4::2])
    p = 2
    while p*2 < z:
        divisor_lst[p] = 0
        for x in range(p+p-1,len(naturalLst),p):
            naturalLst[x] = 0
        p+= 1
        while (naturalLst[p-1]== 0 ):
            p+= 1
    return  list(filter(lambda a:a!= 0, divisor_lst))

#Borrow some stuff from sympy, make it run faster.
#Return prime number...
def findPrime(number):
    return prime(number)

def isPrime(number):
    return isprime(number)
def findPrimeUnder(number):
    i = 0
    not_found = 0
    while prime(i)<number:
        i+=1
    return prime(i-1)

"""
there exist integers x,y such that gcd(a,b) can be written 
as gcd(a,b) = ax + by
extend euclidean algo compute x, and y
"""
def extendEuclideanAlgo(a,b):
	if(b < a):
		a,b = b,a
	if b == 0:
	 	return a,1,0
	x2 = 1	
	x1 = 0
	y2 = 0
	y1 = 1
	while b > 0:
		q = a / b
		r = a - q*b
		x = x2 - q*x1
		y = y2- q*y1
		a = b
		b = r
		x2 = x1
		x1 = x
		y2 = y1
		y1 = y
	return a,x2,y2

