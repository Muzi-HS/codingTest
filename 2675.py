import sys
t = int(input())

for i in range(t):
    n, word = map(str, sys.stdin.readline().split())
    for j in word:
        for k in range(int(n)):
            print("{}".format(j), end='')
    print('')

