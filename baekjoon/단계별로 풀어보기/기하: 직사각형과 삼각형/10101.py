angle = []
for _ in range(3):
    i = int(input())
    angle.append(i)

a = angle[0]
b = angle[1]
c = angle[2]

if a==60 and b==60 and c==60:
    print("Equilateral")
elif a+b+c == 180 and (a==b or b==c or c==a):
    print("Isosceles")
elif a+b+c == 180 and (a != b and b != c and c != a):
    print("Scalene")
elif a+b+c != 180:
    print("Error")