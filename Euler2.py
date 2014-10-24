a = 1
b = 2
temp = 0
sum = 0
while (b < 4000000):
    if( b%2==0):
        sum+= b
    temp = b
    b = a + b
    a = temp
    print(b)
print(sum)
