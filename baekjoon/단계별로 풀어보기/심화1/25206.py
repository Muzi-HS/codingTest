import sys
total = 0
score = 0
change = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
for i in range(20):
    subject, sco, a = map(str,sys.stdin.readline().split())
    if a == 'P':
        continue
    total += float(sco)
    score += float(sco)*change[a]
if total == 0:
    res=0
else:
    res = score/total

print(res)
