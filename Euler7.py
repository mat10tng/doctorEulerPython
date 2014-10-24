primeList = [2,3]
natural = 4;
while len(primeList)<10001:
    for x in primeList:
        isPrime = True
        if natural % x == 0:
            isPrime = False
            break
    if isPrime:
        primeList.append(natural)
        print (natural)
    natural+=1
   
 
