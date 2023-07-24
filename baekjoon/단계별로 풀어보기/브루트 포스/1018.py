import sys
color = ['W','B']
r, c = map(int, input().split())

board = []

for i in range(r):
    line = sys.stdin.readline().replace('\n','')
    board.append(line)

res = []

for i in range(r-7):
    for j in range(c-7):
        resw = 0
        for m in range(i, i+8):
            w = m%2
            for n in range(j, j+8):
                if board[m][n] != color[w]:
                    resw += 1
                w = (w+1)%2
        res.append(resw)
        res.append(64-resw)

print(min(res))