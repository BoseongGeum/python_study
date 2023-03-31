n = 3
p = [0, 0.7, 0.2, 0.1]
dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

for j in range(1, n+1):
    for i in reversed(range(1, j+1)):
        l = []
        for k in range(i, j+1):
            l.append(dp[i][k-1] + dp[k+1][j])
        dp[i][j] = min(l) + sum(p[i:j+1])

print(dp[2][n])
