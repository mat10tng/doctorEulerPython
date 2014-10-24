total = 0
for i in range(2,4*9**5):
	temp = str(i)
	sm = 0
	for char in temp:
		sm+= int(char)**5
	if sm == i:
		total+= i
print(total)
