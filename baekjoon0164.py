import sys
input = sys.stdin.readline
import collections

n, m = map(int, input().split())
l = map(int, input().split())
q = collections.deque([i for i in range(1, n+1)])

cs = 0

for x in l:
    c1 = 0
    c2 = 0
    
    while True:
        if q[0] == x:
            break
        q.rotate(1)
        c1 += 1

    q.rotate(-c1)
    while True:
        if q[0] == x:
            break
        q.rotate(-1)
        c2 += 1
        
    q.popleft()
    
    if c1 < c2:
        cs += c1
    else:
        cs += c2

print(cs)
