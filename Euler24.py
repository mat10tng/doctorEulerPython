from itertools import *
lst = list(permutations("0123456789",10))

print("".join(lst[1000000-1]))