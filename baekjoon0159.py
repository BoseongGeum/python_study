import sys
input = sys.stdin.readline
import collections

n = int(input())
q = collections.deque([i for i in range(1, n+1)])

while True:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    q.rotate(-1)
