n = int(input())

m = n
k=1
while(m>0):
    m -= k
    k += 1
a = n

a -= (k-2)*(k-1)//2
if a == 0:
    if k % 2==0:
        print("{}/{}".format(1, k-2))
    else:
        print("{}/{}".format(k-2,1))
else:
    if k%2==0:
        print("{}/{}".format(k-a,a))
    else:
        print("{}/{}".format(a,k-a))