import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

l = [i for i in range(1, n+1)]
d = deque(l)

for i in range(n):
    d.rotate(-k+1)
    l[i] = d.popleft()

print('<', end='')
for x in l[:len(l)-1]:
    print(x, end=', ')
print(str(l[-1]) + '>')
