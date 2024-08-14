import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

l = [0 for _ in range(n+1)]

for i in range(n):
    l[i], l[i+1] = map(int, input().split())

for d in range(1, n):
    for i in range(n-d):
        j = d + i
        dp[i][j] = sys.maxsize
        
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + l[i] * l[k+1] * l[j+1])

print(dp[0][n-1])
