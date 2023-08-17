import sys

input = sys.stdin.readline

def cntPrime(n):
    prime = [1]*(n+1)
    for i in range(2, int(n**(1/2))+1):
        if prime[i] == 1:
            for j in range(2*i,n+1,i):
                prime[j] = 0
    
    return prime


nums = []

while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)

prime = cntPrime(max(nums)*2+1)

for num in nums:
    res = 0
    for i in range(num+1, 2*num+1):
        res += prime[i]
    print(res)