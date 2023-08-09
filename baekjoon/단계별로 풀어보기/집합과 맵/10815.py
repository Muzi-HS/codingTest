import sys

input = sys.stdin.readline

n = int(input())
sang = sorted(list(map(int, input().split(" "))))
m = int(input())
checks = list(map(int, input().split(" ")))

for check in checks:
    
    #binary search
    left = 0
    right = len(sang)-1
    exist = 0
    while left<=right:
        mid = (left+right)//2
        if sang[mid]>check:
            right = mid -1
        elif sang[mid]<check:
            left = mid + 1
        else:
            exist = 1
            break
    if exist == 1:
        print(1, end = ' ')
    elif exist == 0:
        print(0, end =' ')

# another solution
# import sys

# N = int(sys.stdin.readline())
# cards = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# checks = list(map(int, sys.stdin.readline().split()))

# _dict = {}  # 속도는 dictionary!
# for i in range(len(cards)):
#     _dict[cards[i]] = 0  # 아무 숫자로 mapping

# for j in range(M):
#     if checks[j] not in _dict:
#         print(0, end=' ')
#     else:
#         print(1, end=' ')