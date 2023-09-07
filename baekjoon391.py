import sys
input = sys.stdin.readline

t1, t2, t3 = map(int, input().split())
t = int(input())
s = 0
for _ in range(t):
    ts = 0
    for _ in range(3):
        a, b, c = map(int, input().split())
        ts += a * t1 + b * t2 + c * t3
    if ts > s:
        s = ts

print(s)
