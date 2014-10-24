step = [0]*1000000
step[0] = 1
step[1] = 2
print("hello")
for number in range(3,1000000):
    st = 0
    temp = number
    while temp != 1:
        if temp % 2 == 0:
            temp = temp / 2
            st+=1
            if temp < number:
                st+= step[int(temp-1)]
                break
        else:
            temp = temp*3 +1
            st+=1

    step[number-1] = st
print(step.index(max(step))+1)
