n = int(input())
l = list(input().split())
v = int(input())
c = 0

for x in l:
    if int(x) == v:
        c += 1
    else:
        c = c
print(c)
