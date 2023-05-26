import sys
input = sys.stdin.readline

l = []
for _ in range(9):
    n = int(input())
    l.append(n)

s = sum(l)
for i in range(9):
    for j in range(i+1, 9):
        if s - (l[i] + l[j]) == 100:
            a, b = i, j

del l[b]
del l[a]
for x in sorted(l):
    print(x)
