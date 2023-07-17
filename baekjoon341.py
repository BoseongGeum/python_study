import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

y1 = f*a - d*c
y2 = e*a - b*d

y = y1 // y2
if d == 0:
    x = (c - b*y) // a
else:
    x = (f - e*y) // d

print(x, y)
