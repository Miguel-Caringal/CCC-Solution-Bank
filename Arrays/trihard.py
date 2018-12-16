import pandas as pd

with open("C:\\Users\\Miguel Caringal\\Desktop\\test.txt") as f:
    arr = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
arr = [x.strip() for x in arr]

#twod = [[0 for _ in range(2)] for _ in range(len(arr))]
arr1 = []
arr2 = []
arr3 = []
arr4 = []
arr5 = []

c = 0

def getnum(string):
    finalstring = ""
    for char in string:
        if char.isdigit():
            finalstring+=char
    return(finalstring)

def getseconds(month,day,hour,minuite):
    nummin = 43800 * month + 1440 * day + 24 * hour + minuite
    return nummin

for index in arr:
    guardnumber = ""
    arr[c] = str(arr[c])
    currentdate = arr[c][6:17]
    currentdate = getnum(currentdate)
    month = int(arr[c][6:8])
    day = int(arr[c][9:11])
    hour = int(arr[c][12:14])
    minuite = int(arr[c][15:17])
    numofmins = getseconds(month,day,hour,minuite)
    action = arr[c][19:]
    guardnumber = getnum(action)
    arr1.append(guardnumber)
    if action.find("begins") != -1 or action.find("wakes") != -1:
        arr4.append("start")
    else:
        arr4.append("end")
    arr2.append(int(numofmins))
    arr3.append(minuite)
    arr5.append(day)
    c +=1
myset = set(arr1)
totalzip = zip(arr2,arr1,arr4,arr3,arr,arr5)
totalzip = sorted(totalzip)
timelist,guardlist,statlist,minlist,orig,daylist = (zip(*totalzip))

guardtimelist = []
max = 0

for guard in myset:
    if guard == "":
        continue
    counter = 0
    counterlist = []
    duration = 0
    startpoint = 0
    endpoint = 0
    day = 0
    key = False
    for iguard in guardlist:
        if iguard == guard:
            day = daylist[counter]
            counterlist.append(counter)
        if daylist[counter] == day:
            counterlist.append(counter)
        counter +=1
    for index in counterlist:
        if (statlist[index] == "start"):
            startpoint = timelist[index]
        elif (statlist[index] == "end"):
            endpoint = timelist[index]
            duration += (endpoint - startpoint)
    if duration > max:
        print (guard)
        #print (duration)

df = pd.Datafrane()
df["time"] = timelist
df["guard"] = guardlist
df["stat"] = statlist
df.to_excel("C:\\test.xlsx",index=False)
