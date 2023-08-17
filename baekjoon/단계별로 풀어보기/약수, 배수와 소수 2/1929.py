import sys

input = sys.stdin.readline

def isPrime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0 :
            return 0
    return 1

a, b = map(int,input().split())

for i in range(a, b+1):
    if isPrime(i) == 1:
        print(i)
