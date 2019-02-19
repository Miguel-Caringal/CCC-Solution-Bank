import sys
input = sys.stdin.readline

numlen = int(input())

twodarray = []

vertarray = []

for _ in range(0,numlen):
    temp = input().replace("\n","").split(" ")
    twodarray.append(temp)

for row in range (0,numlen):
    for col in range(0,numlen):
        twodarray[row][col] = int(twodarray[row][col])

#print (twodarray)

for row in range (0,numlen):
    vertarray.append(twodarray[row][0])

horizontalarray = twodarray[0]

#print (vertarray)
#print (horizontalarray)

#print (sorted(horizontalarray))
#print(sorted(vertarray))

if sorted(horizontalarray) == horizontalarray and sorted(vertarray) == vertarray:
    for col in range (0,numlen):
        print (*twodarray[col])
elif sorted (horizontalarray) != horizontalarray and sorted(vertarray) != vertarray:
    for col in range(numlen-1,-1,-1):
        twodarray[col] = sorted(twodarray[col])
        print (*twodarray[col])
elif sorted(horizontalarray) == horizontalarray and sorted(vertarray) != vertarray:
    temptwod = []
    for row in range(numlen-1,-1,-1):
        temp = []
        for col in range (numlen-1,-1,-1):
            temp.append(twodarray[col][row])
        temptwod.append(temp)
    for x in range (numlen-1,-1,-1):
        print (*temptwod[x])
else:
    for row in range(numlen-1,-1,-1):
        temp = []
        for col in range (numlen-1,-1,-1):
            temp.append(twodarray[col][row])
        temp = sorted(temp)
        print (*temp)