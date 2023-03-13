import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*(n+1)
l = [0] + [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(l))

else:
    dp[1] = l[1]
    dp[2] = l[2] + l[1]
    dp[3] = max(l[1] + l[3], l[2] + l[3], l[1] + l[2])

    for x in range(4, n+1):
        dp[x] = max(dp[x-1], dp[x-3] + l[x-1] + l[x], dp[x-2] + l[x])

    print(dp[n])
