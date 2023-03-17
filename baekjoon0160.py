import sys
input = sys.stdin.readline
import collections

n = int(input())

for _ in range(n):
    
    i, j = map(int, input().split())
    q = collections.deque(list(map(int, input().split())))
    k = q[j]
    c = 1
    
    while True:
        
        j -= q.index(max(q))
        q.rotate(-q.index(max(q)))

        if k == max(q) and j == 0:
            print(c)
            break
        
        if j < 0:
            j += (len(q)-1)
        else:
            j -= 1
        q.popleft()
        c += 1
