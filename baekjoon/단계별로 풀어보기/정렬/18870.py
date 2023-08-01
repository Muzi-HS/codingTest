import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

arr_set = set(arr)  # 중복 제거
nums = list(arr_set)  # 리스트 복귀
nums.sort()  # 정렬

numdict = {}

for i in range(len(nums)):  # 딕셔너리 형식으로 인덱스 부여
    numdict[nums[i]] = i
    print(numdict)

for i in arr:
    print(numdict[i], end=' ')  # 인덱스 출력