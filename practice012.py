m = int(input())
n = int(input()) + 1

dp = [[0 for _ in range(n)] for _ in range(n)]
d = [5, 2, 3, 4, 6, 7, 8]

for j in range(1, n):
    for i in reversed(range(1, j)):
        l = []
        for k in range(i, j):
            l.append(dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j])
        dp[i][j] = min(l)

print(dp[m][n-1])
