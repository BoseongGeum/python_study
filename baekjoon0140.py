import sys
input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]
dp = [0]*n

if n <= 2:
    print(sum(l))

else:
    dp[0] = l[0]
    dp[1] = l[1] + l[0]
    dp[2] = l[2] + max(dp[0], dp[1])
    for x in range(3, n):
        dp[x] = max(dp[x-3] + l[x-1], dp[x-2]) + l[x]
    print(dp[n-1])
