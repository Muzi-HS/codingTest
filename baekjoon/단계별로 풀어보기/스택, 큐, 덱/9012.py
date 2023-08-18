import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word = input().rstrip()
    stack = []
    if len(word)%2==1 or word[0] == ')' or word[-1] == '(':
        print('NO')
    else:
        flag = 0
        for i in word:
            if i == ')':
                if stack:
                    stack.pop()
                else:
                    flag = 1
            else:
                stack.append(i)
        
        if stack or flag == 1:
            print('NO')
        else:
            print('YES')

