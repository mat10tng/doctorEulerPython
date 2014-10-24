from sets import Set

def generate_triple(m,n,k):
	a = (m**2 - n**2)*k
	b = 2*n*m*k
	c = (m**2 + n**2)*k
	return sorted([a,b,c])
dct = {}
for m in range(1,251):
	for n in range(1,251):
		k = 1
		sm = 1
		while sm <= 1000 and sm!=0:
			elements = generate_triple(m,n,k)
			sm = sum(elements)
			if sm == 120:
				print(elements)
			if not elements[0]<= 0 and sm <= 1000:
				element = str(', '.join(str(x) for x in elements))
				print(sm)
				if sm not in dct:
					dct[sm]= Set()
				dct[sm].add(element)
			k+=1
print(dct[120])
m = 0
for element in dct.keys():
	if len(dct[element]) > m:
		m = len(dct[element])
		current_element = element
print(current_element)