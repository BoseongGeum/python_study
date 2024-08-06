import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append([w, v])
    
for i in range(1, n+1):
    wi, vi = items[i-1]
    for w in range(k+1):
        if w >= wi:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-wi] + vi)
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])
