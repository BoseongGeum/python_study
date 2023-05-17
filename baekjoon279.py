import sys
input = sys.stdin.readline

s = 0
m = 100
for _ in range(7):
    i = int(input())
    if i % 2 == 1:
        s += i
        if i < m:
            m = i

if s == 0:
    print(-1)
else:
    print(s)
    print(m)
