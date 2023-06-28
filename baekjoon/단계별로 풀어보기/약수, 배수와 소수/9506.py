while(True):
    n = int(input())
    if n==-1:
        break

    arr = []
    total = 0

    for i in range(1, n):
        if n%i ==0:
            total += i
            arr.append(i)

    if total==n:
        print("{} = 1".format(n),end='')
        for k in range(1,len(arr)):
            print(" + {}".format(arr[k]),end='')
        print()
    else:
        print("{} is NOT perfect.".format(n))
