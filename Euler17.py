f = open('Euler17data.txt','r')
dict1 = {}
for line in f:
    line  = line.strip().split()
    dict1[int(line[0])]  = len(line[1])
    
print (dict1)



# this work for all element under 100
def numbersLength(numbers, dict1):
    if numbers < 21 or numbers%10 == 0:
        return dict1[numbers]
    else:
        return dict1[numbers - numbers%10] + dict1[numbers%10]      
    

sm = 0
for number in range(1,1000):
    if number <= 100:
        sm+= numbersLength(number, dict1)
    elif number%100 == 0:
        sm+= numbersLength(number/100, dict1)+len("hundred")
    else:
        print(number, number%100)
        sm+= dict1[(number-number%100)/100]+ numbersLength(number%100, dict1)+len("hundredand")
print(sm+len("onethousand"))
