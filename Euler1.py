a = 1
sum = 0;
while (a*3 < 1000 or a*5 < 1000) :
        if a*3 % 5 == 0:
                sum-=a*3
        if a*3 < 1000:
                sum+=a*3
        if a*5 < 1000:
                sum+=a*5
        a+=1
print (sum)
