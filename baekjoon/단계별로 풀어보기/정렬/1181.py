import sys
n = int(input())
order = []
res ={}
for _ in range(n):
    word = sys.stdin.readline().replace('\n','')
    if len(word) not in res:
        res[len(word)] = []
        order.append(len(word))
    if word in res[len(word)]:
        continue
    res[len(word)].append(word)
order.sort()
result = []
for i in order:
    res[i].sort()
    for j in res[i]:
        result.append(j)

for k in result:
    print(k)

