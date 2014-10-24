#Annat algoritm för problem 18
f = open('Euler67Data.txt', 'r')
lst = list()
for line in f:
    line = line.strip().split()
    line = [int(i) for i in line]
    lst.append(line)
mx= [0]

for rowIndex in reversed(range(len(lst)-1)):
    for elementIndex in range(len(lst[rowIndex])):
        lst[rowIndex][elementIndex] = lst[rowIndex][elementIndex] + max(lst[rowIndex+1][elementIndex], lst[rowIndex+1][elementIndex+1])
print (lst[0])
