import sys
input = sys.stdin.readline

n = int(input())

a = int(input())
b = int(input())
c = int(input())

if c + a == 2 * b:
    g = b - a
    s = 0
else:
    g = b // a
    s = 1
if n != 3:
    for _ in range(n - 4):
        int(input())
    f = int(input())
else:
    f = c
    
if s == 0:
    print(f + g)
else:
    print(f * g)
