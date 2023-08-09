import sys

input = sys.stdin.readline

n, m = map(int,input().split())

string = {}

for _ in range(n):
    string[input().rstrip()] = 0

for _ in range(m):
    word = input().rstrip()
    if word in string:
        string[word] += 1

total = 0
for i in string:
    total += string[i]

print(total)