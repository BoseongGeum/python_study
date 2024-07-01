import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())

for _ in range(t):
    
    m, n, k = map(int, input().split())
    maps = [[0 for _ in range(m)] for _ in range(n)]
    
    for _ in range(k):
        
        x, y = map(int, input().split())
        maps[y][x] = 1

    count = 0
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    def dfs(i, j):
        
        maps[j][i] = 2

        for di, dj in dirs:
            nexti, nextj = i+di, j+dj
            
            if 0 <= nexti < m and 0 <= nextj < n and maps[nextj][nexti] == 1:
                dfs(nexti, nextj)

    for j in range(n):
        for i in range(m):
            if maps[j][i] == 1:
                dfs(i, j)
                count += 1

    print(count)
