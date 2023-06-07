import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    money = int(input())
    print(money//25,end=' ')
    print((money%25)//10,end=' ')
    print(((money%25)%10)//5,end=' ')
    print(((money%25)%10)%5)

