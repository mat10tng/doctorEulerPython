from doctorNumber import *
f = open('Euler89.txt', 'r')
lst = list()
for line in f:
    lst.append(toArray(int(line)))
answer_lst = lst.pop(0)
print(answer_lst)
print(lst)
current_index = 0
found = 0
while found!= 100:
	element = lst[current_index]
	for i in range(len(answer_lst)-1):
		for j in range(1,len(answer_lst)):
			if element[0] == answer_lst[i] and element[2] == answer_lst[j]:
				answer_lst.insert(i+1,element[1])
				lst.pop(current_index) 
				
	current_index = (current_index+1) %len(lst)
	found +=1
print(lst)