n = int(input())
l = []
for x in range(n):
    a,b=map(int, input().split())
    l.append(a)
    l.append(b)
for x in range(n):
    print(l[0]+l[1])
    del l[0:2]
