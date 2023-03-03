import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = map(int, input().split())
l = []
s = 0
c = 0

for x in a:
    s += x
    y = s % m
    for z in l:
        if y == z:
            c += 1
    l.append(y)
c += l.count(0)
print(c)
