from functools import reduce
f = open('Euler8data.txt','r')
data = list(map(int,f.readlines()))
answerLst =list()
newData = list()
for information in data :
    newData = newData + [int(i) for i in list(str(information))]
print(newData)

while len(newData) >= 10:
    answerLst.append(reduce(lambda x, y: x*y , newData[:-1]))
    newData.pop(0)
print(max(answerLst))
