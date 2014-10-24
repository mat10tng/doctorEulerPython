from functools import reduce
def factorial(n): return reduce(lambda x,y:x*y, range(1,n+1))
# there is 20 different way to right ,20 down. How many ways is there ?
print (factorial(40)/(factorial(20)**2))
