a,b,c = map(int, input().split())

if a>b:
    if c>a:
        max = c
        r = a+b
    else:
        max = a
        r = b+c
else:
    if c>b:
        max = c
        r = a+b
    else:
        max = b
        r = a+c

while True:
    if r>max:
        print(r+max)
        break
    else:
        max -= 1


