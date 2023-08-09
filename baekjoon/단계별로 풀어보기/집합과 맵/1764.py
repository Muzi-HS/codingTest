import sys

input = sys.stdin.readline

n, m = map(int, input().split())

info = {}

for _ in range(n):
    name = input().rstrip()
    info[name] = 0

res = []

for _ in range(m):
    name = input().rstrip()
    if name in info:
        res.append(name)

print(len(res))
res.sort()
for i in res:
    print(i)


# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr1 = []
# arr2 = []
# for i in range(n):
#     x = input()
#     arr1.append(x)
# for i in range(m):
#     y = input()
#     arr2.append(y)

# answer = list(set(arr1) & set(arr2))
# answer.sort()
# print(len(answer))
# print(''.join(answer), end = '')