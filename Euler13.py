f = open('Euler13data.txt','r')
data = list()
for line in f:
    line = line.strip()
    line= [int(i) for i in str(line)]
    data.append(line)

data1=reversed(list( zip(*data)))
firstTenDigits = 0
tenExpo = 0
for row in data1:
    firstTenDigits+=sum(row)*10**tenExpo
    tenExpo+=1
    if len(str(firstTenDigits)) > 10:
        print("hello")
        firstTenDigits = int(str(firstTenDigits)[:-1])
        tenExpo-=1
    print (firstTenDigits)
