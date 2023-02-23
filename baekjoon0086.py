xl = []
yl = []

for _ in range(3):
    x,y = map(int, input().split())
    if x in xl:
        xl.remove(x)
    else:
        xl.append(x)
    if y in yl:
        yl.remove(y)
    else:
        yl.append(y)
    
print(xl[0], yl[0])
