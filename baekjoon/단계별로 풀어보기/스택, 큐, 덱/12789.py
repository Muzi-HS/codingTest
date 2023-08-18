import sys 

input = sys.stdin.readline

n = int(input())
line = list(map(int,input().split()))
visited = sorted(line)
stack = []

while True:
    if visited:
        if line:
            if visited[0] == line[0]:
                visited.pop(0)
                line.pop(0)
            else:
                if stack:
                    if visited[0] == stack[-1]:
                        visited.pop(0)
                        stack.pop()
                    else:
                        if line:
                            stack.append(line.pop(0))
                        else:
                            print('Sad')
                            break
                else:
                    stack.append(line.pop(0))
        else:
            if stack:
                if visited[0] == stack[-1]:
                        visited.pop(0)
                        stack.pop()
                else:
                    print('Sad')
                    break
            else:
                print('Nice')
                break
    else:
        print('Nice')
        break
