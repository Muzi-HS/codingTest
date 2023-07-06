a, b = map(int, input().split())
c = int(input())
n = int(input())

if (b<=0 and c>=a) or (b>0 and c>a and n>=b/(c-a)):
    print(1)
else:
    print(0)