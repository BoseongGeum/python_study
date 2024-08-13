import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    s = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        s[i] = s[i-1] + l[i-1]

    for d in range(1, n):
        for i in range(n-d):
            j = i + d
            dp[i][j] = sys.maxsize

            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + s[j+1] - s[i])

    print(dp[0][n-1])
