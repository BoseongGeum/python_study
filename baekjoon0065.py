m = int(input())
n = int(input())
l = []
for x in range(m,n+1):
    if x == 2:
        l.append(x)
        continue
    for y in range(2, x):
        if x % y == 0:
            break
        elif y == x - 1:
            l.append(x)
if l == []:
    print(-1)
else:
    print(sum(l))
    print(l[0])
