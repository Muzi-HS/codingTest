import sys

input = sys.stdin.readline

n = int(input())

def gcd(a, b):
    for x in range(1,min(a,b)+1):
        if a%x==0 and b%x==0:
            res = x
    return res

def lcm(a, b):
    res = a*b//gcd(a,b)
    return res

for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))