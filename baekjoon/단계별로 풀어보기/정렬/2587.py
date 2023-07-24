res = []
for _ in range(5):
    res.append(int(input()))

print(sum(res)//5)
res.sort()
print(res[2])
