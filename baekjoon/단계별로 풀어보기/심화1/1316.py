import sys
n = int(input())
res = n

for i in range(n):
    word = sys.stdin.readline()
    rec = []
    rec.append(word[0])
    for j in range (1, len(word)-1):
        if word[j] != word[j-1]:
            if word[j] not in rec:
                rec.append(word[j])
            elif word[j] in rec:
                n -=1
                break
        elif word[j] == word[j-1]:
            continue
print(n)