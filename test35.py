def solution(n, computers):
    visited = [0 for _ in range(n)]
    count = 0
    
    def dfs(com):
        for i in range(n):
            if computers[com][i] == 1:
                computers[com][i] = 0
                computers[i][com] = 0
                dfs(i)
    
    for j in range(n):
        if computers[j][j] == 1:
            dfs(j)
            count += 1
    
    return count
