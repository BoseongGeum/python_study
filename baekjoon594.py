import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maps[i] = list(map(int, input().split()))

queue = deque()
count = 0

for x in range(n):
    for y in range(m):
        if maps[x][y] == 1:
            queue.append([x, y, 0])
        elif maps[x][y] == 0:
            continue
        count += 1

totalDay = 0

while queue:
    x, y, day = queue.popleft()

    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
            queue.append([nx, ny, day+1])
            maps[nx][ny] = 1
            count += 1

    totalDay = day

if count == m * n:
    print(totalDay)
else:
    print(-1)
