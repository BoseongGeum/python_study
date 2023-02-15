m,n = map(int, input().split())

l = []
for x in range(m, n+1):
    if x == 2:
        l.append(x)
        continue
    for y in range(2, x):
        if x%y == 0:
            del 
            break
print(*l, sep='\n')
