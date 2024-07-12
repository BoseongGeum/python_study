import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

maps = [0 for _ in range(max(n, k)*2+1)]
maps[n] = 1

queue = deque()
queue.append([n, 0])

while queue:
    x, count = queue.popleft()

    if x == k:
        print(count)
        break

    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < len(maps) and maps[nx] == 0:
            queue.append([nx, count+1])
            maps[nx] = 1
