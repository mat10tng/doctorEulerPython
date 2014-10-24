from doctorNumber import *
set1 = {1}
set89 = {89}
temp_chain = list()
for i in range(2,10**7+1):
	found = False
	number = i
	temp_chain.append(number)
	while not found:
		if number in set1:
			found = True
			set1 |= set(temp_chain)
		elif number in set89:
			found = True
			set89 |= set(temp_chain)
		number = find_next_chain_number(number)
		temp_chain.append(number)

	temp_chain = list()
print(len(set89))
print(len(set1))
print(len(set89)+len(set1))