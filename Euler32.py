from itertools import *
from doctorNumber import *
from doctorPandigital import *
#The maximum can not have length bigger than (size -leftside)/2

number = "123456789"
#Left * Right = Result
st = set()
sm  = 0
for x in range(1,5):
	permu_left = number_permutations("123456789", x)
	for left in permu_left:
		leftSet = toSet(left)
		rightSet =toSet(number).difference(leftSet)
		right = toNumber(rightSet)
		for y in range(1,5):
			right_permutation = number_permutations(right,y)
			for r in right_permutation:
				product = r*left
				super = str(left)+str(r)+str(product)
				if  is_pandigital(super):
					sm+= 0
					if len(super ) == 9:
						st.add(product)
						print(left,r,product,super,"-----")

print(sm)
print(sum(st))