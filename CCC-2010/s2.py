length1 = int(input())

dictionary = {}

for _ in range(0,length1,1):
    string = str(input())
    char, sequence = string.split(" ")
    dictionary[sequence] = char

inputstring = str(input())
outputstring = ""
pos = 0

length = len(inputstring)

while (pos!= length):
    gate = False
    i = 0
    currentsubset = ""
    while gate == False:
        currentsubset += inputstring[pos+i]
        #print (outputstring)
        if currentsubset in dictionary:
            #print (currentsubset)
            outputstring += dictionary[currentsubset]
            #print (outputstring)
            i += 1
            break
        i += 1
    pos += i

print (outputstring)