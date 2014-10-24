prime = 2
number = 600851475143
primeFactor= []
while (number != 1):
    if(number % prime == 0 ):
        primeFactor.append(prime)
    while(number % prime == 0):
        number = number /prime
    prime+= 1
print (primeFactor)



