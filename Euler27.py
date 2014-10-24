
rnge =int( (1001+1) /2)
sm = 1
lastNumber = 1
pow = 1
for i in range(1,rnge):
	for j in range(1,5):
		lastNumber = lastNumber+2*pow
		sm+= lastNumber
		print(lastNumber)
	pow+=1
print(sm)