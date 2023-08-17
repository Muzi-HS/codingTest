import sys

input = sys.stdin.readline

b, a = map(int,input().split())
d, c = map(int,input().split())

def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while(b>0):
        a,b = b, a%b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)


m = lcm(a,c)
n = lcm(a,c)//a*b+lcm(a,c)//c*d

print("%d %d"%(n//gcd(m,n),m//gcd(m,n)))