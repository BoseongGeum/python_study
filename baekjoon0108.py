import sys
input = sys.stdin.readline

n,m = map(int, input().split())
x = 1
a = x
l = []

for y in range(1, n+1):
    x *= y
    if y == m or y == n - m:
        if m == n - m:
            l.append(x)
        l.append(x)
for y in l:
    a *= y
print((x//a) % 10007)
