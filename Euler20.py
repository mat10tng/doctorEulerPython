from functools import reduce
print(sum(map(int,str(reduce(lambda a,b:a*b,range(1,101))))))

 