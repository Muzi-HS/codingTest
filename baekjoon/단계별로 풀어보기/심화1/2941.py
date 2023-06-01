word = input()
crolist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in crolist:
    word = word.replace(i, '*')

print(len(word))
