import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
maps = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    xmin, ymin, xmax, ymax = map(int, input().split())

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
            maps[y][x] = 1

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    
def dfs(x, y):
    global count

    maps[y][x] = 1
        
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 0:
            dfs(nx, ny)
            count += 1

countList = []

for x in range(n):
    for y in range(m):
        if maps[y][x] == 0:
            count = 1
            dfs(x, y)
            countList.append(count)

print(len(countList))
print(*sorted(countList))
