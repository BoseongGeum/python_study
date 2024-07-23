import sys
input = sys.stdin.readline

r, c = map(int, input().split())

maps = [[0 for _ in range(c)] for _ in range(r)]

for i in range(r):
    maps[i] = list(input().rstrip())

visited = set()
visited.add(maps[0][0])

dirs = [[1,0],[-1,0],[0,1],[0,-1]]
maxDep = 0

def dfs(x, y, dep, visited):
    global maxDep
    
    maxDep = max(maxDep, dep)

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy

        if 0 <= nx < r and 0 <= ny < c:
            char = maps[nx][ny]
            
            if char not in visited:
                visited.add(char)
                dfs(nx, ny, dep+1, visited)
                visited.remove(char)

dfs(0, 0, 1, visited)
print(maxDep)
