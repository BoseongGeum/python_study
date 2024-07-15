import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maps[i] = list(map(int, list(input().rstrip())))

queue = deque()
queue.append([0, 0])

while queue:
    x, y = queue.popleft()

    if x == n-1 and y == m-1:
        print(maps[x][y])
        break

    for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
            maps[nx][ny] = maps[x][y]+1
            queue.append([nx, ny])
