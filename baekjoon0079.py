n = int(input())
l = []
for x in range(n):
    a, b = map(int, input().split())
    l.append([b,a])
for x in sorted(l):
    print(x[1], x[0])
