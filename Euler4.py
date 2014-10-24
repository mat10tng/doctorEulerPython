
palin = []
for a in range (900,999):
    for b in range (900,999):
        temp = str(a*b)
        if temp == temp[::-1]:
            palin.append(temp)
print(palin)
