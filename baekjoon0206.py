import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

i = 1
s = 1
t = []
while s <= m:
    if s >= n:
        t.append(s)
    i += 1
    s = i ** 2

if t == []:
    print(-1)
else:
    print(sum(t))
    print(t[0])
