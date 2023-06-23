import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int,input().split())
q = deque()

if b > a:
    print(b - a - 1)
    for i in range(a+1, b):
        q.append(i)
    print(*q)
elif b == a:
    print(0)
    print()
else:
    print(a - b - 1)
    for i in range(b+1, a):
        q.append(i)
    print(*q)
