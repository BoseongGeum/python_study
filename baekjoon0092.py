n, m = map(int, input().split())
a = ['W','B']*(int(n*m/2)+1)
c = 0
l = []
for x in range(n):
    l.append(list(input()))
    
l1 = sum(l, [])
for x in range(n):
    for y in range(m):
        if m % 2 == 0 and x % 2 == 1:
            if l1[x*m + y] != a[x*m + y+1]:
                c += 1
        else:
            if l1[x*m + y] != a[x*m + y]:
                c += 1

c2 = n*m - c
if c > c2:
    print(c2)
else:
    print(c)
