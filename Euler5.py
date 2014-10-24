from functools import reduce
prim = [2,3,5,7,11,13,17,19]
primX = list()
li = list((range(1,21)))
new =list()
print (li)
for  x in prim:
    for y in li:
        temp = 0
        print(y , x)
        while y % x == 0:
            y = y / x
            temp+=1
        new.append(temp)
    primX.append(max(new))
    new = list()
print(prim)
print(primX)
answer = reduce(lambda x, y: x*y, [i**j for i, j in zip(prim, primX)])
print(answer)
