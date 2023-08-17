import sys

def isPrime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return 0
    return 1

input = sys.stdin.readline

n = int(input())


nums = []

for _ in range(n):
    num=int(input())
    while True:
        if isPrime(num) == 1:
            nums.append(num)
            break
        num += 1

for i in nums:
    print(i)