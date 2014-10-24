count = 0 
sum = 200
for x200 in range (200,-1,-200):
	for x100 in range(x200 ,-1,-100):
		for x50 in range(x100,-1,-50):
			for x20 in range(x50,-1,-20):
				for x10 in range(x20,-1,-10):
					for x5 in range(x10,-1,-5):
						for x2 in range(x5,-1,-2):
							count+=1
print(count)

sum = 200
coins = [1 ,2 ,5 ,10 ,20 , 50, 100 , 200]
way = [0]*201
# how many change for 0p can u give using 1p. define as 1
way[0] = 1

for index in range(len(coins)):
	for change in range(coins[index],201):
		way[change] = way[change] +  way[change - coins[index]]
print (way)