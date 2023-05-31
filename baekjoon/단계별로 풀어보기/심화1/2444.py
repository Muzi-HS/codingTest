n = int(input())

for i in range(n):
    print("{}{}".format(' '*(n-1-i),'*'*(2*i+1)))
for j in range(n-1):
    print('{}{}'.format(' '*(j+1),'*'*((n-1-j)*2-1)))

"""

n = int(input())

for i in range(n):
    print(' '*(n-1-i),'*'*(2*i+1))
for j in range(n-1):
    print(' '*(j+1),'*'*((n-1-j)*2-1))


각 줄의 맨 앞에 불필요한 공백이 생긴다.
print(1,2,3)
output : 1 2 3
"""