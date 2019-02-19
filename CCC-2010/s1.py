numcomp = int(input())

maxsum = 0
maxsumname = ""
secondsum = 0
secondsumname = ""
testarr = []

for _ in range(0,numcomp,1):
    string = str(input())
    name,ram,cpu,disk = string.split(" ")
    ram = int(ram)
    cpu = int(cpu)
    disk = int(disk)
    sum = ram*2+cpu*3+disk
    if sum > maxsum:
        testarr = []
        secondsumname = maxsumname
        secondsum = maxsum
        maxsumname = name
        maxsum = sum
    elif sum < maxsum and sum > secondsum:
        secondsumname = name
        secondsum = sum
    elif sum == maxsum:
        if testarr == []:
            testarr.append(maxsumname)
        testarr.append(name)

if not testarr:
    arr = [maxsumname,secondsumname]
    if maxsum == secondsum:
        arr.sort()

    for index in arr:
        if index is not "":
            print (index)
else:
    testarr.sort()
    for index in range(0,2,1):
        print (testarr[index])

