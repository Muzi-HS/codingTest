word = input()
for i in range(97, 123): #chr(97)=a,chr(122)=z
    if chr(i) in word:
        print("{}".format(word.index(chr(i))), end= ' ')
    else:
        print("-1", end = ' ')
