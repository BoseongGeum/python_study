import sys
input = sys.stdin.readline

n, m = map(int, input().split())

l1 = []
for _ in range(n):
    l1.append(list(map(int, input().split())))
l2 = [0]
for x in l1:
    l3 = [0]
    s = 0
    for y in x:
        s += y
        l3.append(s)
    l2.append(l3)

for _ in range(m):
    s = 0
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2+1):
        s += l2[x][y2] - l2[x][y1-1]
    print(s)
