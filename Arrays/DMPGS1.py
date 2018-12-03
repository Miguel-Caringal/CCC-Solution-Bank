def main():
    from sys import stdin, stdout, maxsize
    len = int(stdin.readline())
    str = stdin.readline()
    list = str.split()
    list.sort()
    mindiff = maxsize
    counter = 0
    c2 = 0
    for _ in list:
        list [c2] = int(list[c2])
        c2 +=1
    for _ in range(0,len-1):
        currentsum = list[counter] - list[counter+1]
        currentsum = abs(currentsum)
        if currentsum < mindiff:
            mindiff = currentsum
        counter +=1
    print(mindiff)

if __name__ == "__main__":
    main()