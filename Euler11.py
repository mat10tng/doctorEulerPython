from functools import reduce
f = open('Euler11data.txt','r')
data = list()
for line in f:
    line = line.strip()
    line = line.split(' ')
    line= [int(i) for i in line]
    data.append(line)
    
maxRight = 0
maxDown = 0
data1 = list(zip(*data))

mx = 0
for i in range(0,16):
    for j in range(0,16):
        multiRight =data[i][j]*data[i][j+1]*data[i][j+2]*data[i][j+3]
        multiDown = data[i][j]*data[i+1][j]*data[i+2][j]*data[i+3][j]
        multiDiagDown = data[i][j]*data[i+1][j+1]*data[i+2][j+2]*data[i+3][j+3]
        multiDiagUpp = data[i+3][j]*data[i+2][j+1]*data[i+1][j+2]*data[i][j+3]
        if mx < multiRight:
            mx = multiRight
        elif mx < multiDown:
            mx = multiDown
        elif mx < multiDiagDown:
            mx = multiDiagDown
        elif mx < multiDiagUpp:
            mx = multiDiagUpp
        print(mx)
