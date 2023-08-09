import sys

input = sys.stdin.readline

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = list(set(a)&set(b))
print(len(a)+len(b)-len(res)*2)
