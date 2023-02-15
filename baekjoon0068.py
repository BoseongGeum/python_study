n,m = map(int, input().split())

l1 = []
l2 = []
for x in range(n):
    a = list(map(int, input().split()))
    l1.append(a)
for x in range(n):
    b = list(map(int, input().split()))
    l2.append(b)
for x in range(n):
    for y in range(m):
        print(l1[x][y] + l2[x][y], end=' ')
    print()
