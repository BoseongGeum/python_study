import sys
input = sys.stdin.readline
import collections

n, m = map(int, input().split())

l = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    
    d = collections.deque(l[i-1:j])
    d.rotate(i - k)
    l[i-1:j] = list(d)
    
print(*l)
