xspot=[]
yspot=[]
for _ in range(3):
    x,y = map(int,input().split())
    xspot.append(x)
    yspot.append(y)
resx =[]
resy = []
for i in range(3):
    if xspot.count(xspot[i])==1:
        resx.append(xspot[i])
    if yspot.count(yspot[i])==1:
        resy.append(yspot[i])
print("{} {}".format(resx[0],resy[0]))