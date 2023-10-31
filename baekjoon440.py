import sys
input = sys.stdin.readline

d1, d2, d3 = map(float, input().split())

s = d1 + d2 + d3
a = d1 + d2 - s/2
b = d1 + d3 - s/2
c = d2 + d3 - s/2

if a > 0 and b > 0 and c > 0:
    print(1)
    print(round(a, 1), round(b, 1), round(c, 1))
else:
    print(-1)
