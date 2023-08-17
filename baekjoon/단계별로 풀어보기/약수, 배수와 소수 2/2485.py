import sys

input = sys.stdin.readline

def gcd(a,b):
    a, b  = max(a,b),min(a,b)
    while(b>0):
        a,b=b,a%b
    return a

n = int(input())

diff = []

num = int(input())

for _ in range(n-1):
    m = int(input())
    diff.append(m - num)
    num = m

tmpgcd = diff[0]

for i in range(1,len(diff)):
    tmpgcd = gcd(tmpgcd,diff[i])

print((sum(diff)-len(diff)*tmpgcd)//tmpgcd)
