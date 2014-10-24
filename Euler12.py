from TriForce import *
from doctorPrime import *

currentNumber = 1
nextNumber= 2
primeBelow = findPrimeBelow(75000)
while True:
    currentNumber += nextNumber
    nextNumber+=1
    temp = currentNumber
    numberOfDiv = 1
    for x in primeBelow:
        if temp  == 1:
            break
        exp = 1
        while temp % x == 0:
            exp+= 1
            temp = temp/x
        numberOfDiv*=exp
    print(currentNumber)
    if numberOfDiv>500:
        print(currentNumber)
        break;