#Annat algorith för problem 67
f = open('Euler18Data.txt', 'r')
lst = list()
for line in f:
    line = line.strip().split()
    line = [int(i) for i in line]
    lst.append(line)
mx= [0]
sm = 0
def recursion(currentRowIndex,currentElementIndex,sm,lst,mx):
    #Basfall när vi är vid sista element i pyramiden
    if currentRowIndex == len(lst)-1:
        if mx[0] < sm+lst[currentRowIndex][currentElementIndex]:
            mx[0] = sm+lst[currentRowIndex][currentElementIndex]
            print(mx[0])
    else:
        sm+= lst[currentRowIndex][currentElementIndex]
        #vänster
        recursion(currentRowIndex+1,currentElementIndex,sm,lst,mx)
        #höger
        recursion(currentRowIndex+1,currentElementIndex+1,sm,lst,mx)
recursion(0,0,0,lst,mx)
print(mx[0])
