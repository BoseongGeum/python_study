import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    
    i = int(input())
    maps = [[0 for _ in range(i)] for _ in range(i)]

    ix, iy = map(int, input().split())
    tx, ty = map(int, input().split())

    queue = deque()
    queue.append([ix, iy])

    while queue:
        x, y = queue.popleft()

        if x == tx and y == ty:
            print(maps[x][y])
            break

        for dx, dy in [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < i and 0 <= ny < i and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y]+1
                queue.append([nx, ny])
