def solution(m, n, puddles):
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for [i,j] in puddles:
        dp[i][j] = -1
    for i in range(m):
        dp[i][0] = -1
    for i in range(n):
        dp[0][i] = -1
    dp[1][1] = 1
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if dp[i][j] == 0:
                if dp[i][j-1] > 0 and dp[i-1][j] > 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif dp[i][j-1] > 0:
                    dp[i][j] = dp[i][j-1]
                elif dp[i-1][j] > 0:
                    dp[i][j] = dp[i-1][j]
    print(dp)
    
    return dp[m][n] % 1000000007

solution(4,3, [[2,2]])
