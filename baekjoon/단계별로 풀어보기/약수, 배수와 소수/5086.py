import sys

while(True):
    a, b = map(int, sys.stdin.readline().split())
    if a<b and b%a==0:
        print("factor")
    elif a>b and a%b==0:
        print("multiple")
    elif a==0 and b==0:
        break
    else:
        print("neither")