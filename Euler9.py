lst = list()
m=1
while m < 501:
    if 500 % m == 0:
        n = 500/m - m
        if m > n and n>0:
            lst.append(m)
            lst.append(n)
    m+=1
print(lst)
# generate a, b , c from previous m and n
lst_abc = list()
x = len(lst)//2
print(x)
for i in range(0, x):
    m= lst[2*i]
    n=lst[2*i+1]
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    print(a,b,c)
    if a**2 + b**2 == c**2:
        if a + b + c == 1000:
            print(a*b*c)
