n = int(input())
l = []
for x in range(n):
    a, b = map(int, input().split())
    l.append([a,b])
for x in sorted(l):
    print(*x, sep=' ')
