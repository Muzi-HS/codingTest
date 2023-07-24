n, k = map(int, input().split())

res = list(map(int, input().split(' ')))

res.sort()
print(res[n-k])