import sys

input = sys.stdin.readline

n = int(input())

record = {}

for _ in range(n):
    name, state = map(str,input().rstrip().split())
    record[name] = state
    if state == 'leave': del record[name]

# key를 기준으로 내림차순 정렬(reverse=True)하고 내림차순 정렬된 key값들의 리스트 생성
result = sorted(record.keys(), reverse=True)

for i in result:
    print(i)