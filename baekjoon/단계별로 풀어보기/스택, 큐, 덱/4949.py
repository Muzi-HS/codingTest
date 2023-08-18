import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    stack = []
    flag = 0
    if string == '.':
        break
    else:
        for i in string:
            if i == '[' or i == '(':
                stack.append(i)
            elif i == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        flag = 1
                        break
                else:
                    print('no')
                    flag = 1
                    break
            elif i == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        flag = 1
                        break
                else:
                    print('no')
                    flag = 1
                    break
            else:
                continue
        if stack and flag == 0:
            print('no')
        elif flag == 0:
            print('yes')
            
