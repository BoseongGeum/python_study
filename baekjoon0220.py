import sys
input = sys.stdin.readline

n = int(input())
l = []
overlap = 0

for _ in range(n):
    a, b = map(int, input().split())
    l.append([a, b])

for x in range(n):
    for y in range(x+1, n):
        if abs(l[x][0] - l[y][0]) < 10 and abs(l[x][1] - l[y][1]) < 10:
            overlap += (min(l[x][0], l[y][0]) + 10 - max(l[x][0], l[y][0])) * (min(l[x][1], l[y][1]) + 10 - max(l[x][1], l[y][1]))

print(100 * n - overlap)
