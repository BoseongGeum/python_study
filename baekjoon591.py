import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

maps1 = []
maps2 = []

n = int(input())
for _ in range(n):
    l = list(input().rstrip())
    maps1.append(l[::])
    
    for i in range(n):
        if l[i] == 'R':
            l[i] = 'G'
    maps2.append(l[::])

dirs = [[0,1],[0,-1],[1,0],[-1,0]]
    
def dfs(x, y, color):
    global count

    maps[y][x] = 'V'
        
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and maps[ny][nx] == color:
            dfs(nx, ny, color)
            
count = 0
maps = maps1[::]

for x in range(n):
    for y in range(n):
        if maps[y][x] != 'V':
            dfs(x, y, maps[y][x])
            count += 1
            
normal = count

count = 0
maps = maps2[::]

for x in range(n):
    for y in range(n):
        if maps[y][x] != 'V':
            dfs(x, y, maps[y][x])
            count += 1

print(normal, count)
