import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    maps[i] = list(input().rstrip())

maxLen = 0

for i in range(n):
    for j in range(m):

        tempMaps = [[0 for _ in range(n)] for _ in range(m)]
        for k in range(n):
            tempMaps[k] = maps[k][:]
        
        queue = deque()
        if tempMaps[i][j] == 'L':
            queue.append([i,j,0])

        while queue:
            x, y, dis = queue.popleft()

            maxLen = max(maxLen, dis)

            for dx, dy in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx, ny = x+dx, y+dy

                if 0 <= nx < n and 0 <= ny < m and tempMaps[nx][ny] == 'L':
                    queue.append([nx,ny,dis+1])
                    tempMaps[nx][ny] = 'V'

print(maxLen)
