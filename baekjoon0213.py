import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)

dp[0] = 0
dp[1] = 1

if n < 2:
    print(dp[n])

else:
    for x in range(2, n+1):
        dp[x] = dp[x-1] + dp[x-2]

    print(dp[n])
