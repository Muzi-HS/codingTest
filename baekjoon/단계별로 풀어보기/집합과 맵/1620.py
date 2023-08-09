import sys

input = sys.stdin.readline

n, m = map(int,input().split())

dictionary = {}

for i in range(n):
    poketmon = input().rstrip()
    dictionary[i+1] = poketmon

# reversed dictionary
reversed_dictionary = {p:num for num,p in dictionary.items()}

for _ in range(m):
    answer = input().rstrip()
    if 64<ord(answer[0]) and ord(answer[0])<91:
        print(reversed_dictionary[answer])
    else:
        print(dictionary[int(answer)])