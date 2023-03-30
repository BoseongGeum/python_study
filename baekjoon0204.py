import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    v = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(v[0][0], v[1][0]))
        
    else:
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = v[0][0]
        dp[0][1] = v[1][0]
        dp[1][1] = dp[0][0] + v[1][1]
        dp[1][0] = dp[0][1] + v[0][1]
        for x in range(2, n):
            dp[x][0] = max(dp[x-2][1] + v[0][x], dp[x-1][1] + v[0][x])
            dp[x][1] = max(dp[x-2][0] + v[1][x], dp[x-1][0] + v[1][x])

        print(max(dp[n-1]))
