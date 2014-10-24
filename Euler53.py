import math
# math.factorial(n)
fact_array =[math.factorial(a) for a in range(101)]

count = 0
for n in range(1,101):
	for r in range(1,n+1):
		result = fact_array[n]/(fact_array[r]*fact_array[n-r])
		if result > 1000000:
			count+=1
	print(n)
print(count)