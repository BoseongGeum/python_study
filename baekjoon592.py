import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
maps = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    maps[i] = list(map(int, input().rstrip()))

complexCount = 0
areaCount = 0
countList = []

dirs = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(x, y):
    global areaCount

    maps[x][y] = 2
    areaCount += 1

    for dx, dy in dirs:
        nx, ny = dx+x, dy+y

        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
            dfs(nx, ny)

for x in range(n):
    for y in range(n):
        if maps[x][y] == 1:
            complexCount += 1
            areaCount = 0
            
            dfs(x, y)
            countList.append(areaCount)

print(complexCount)
for count in sorted(countList):
    print(count)
