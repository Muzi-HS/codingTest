import sys
n = int(input())

for i in range(n):
    word = sys.stdin.readline()
    print(word[0],end='')
    print(word[-2])