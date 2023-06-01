import sys
c = int(input())

for i in range(c):
    score = list(map(int,sys.stdin.readline().split()))
    total = 0
    for j in range(len(score)-1):
        total = total + score[j+1]
    avg = total/score[0]
    cnt = 0
    for k in range(len(score)-1):
        if score[k+1]>avg:
            cnt +=1
    print("{:.3f}%".format(cnt/score[0]*100))