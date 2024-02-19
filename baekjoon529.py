import sys
input = sys.stdin.readline

dp = [0] * 101
while True:
    n = int(input())
    if n == 0:
        break
    elif n == 1:
        dp[1] = 1
    elif dp[n-1] != 0:
        dp[n] = dp[n-1] + n ** 2
    else:
        for i in range(1, n+1):
            if dp[i] != 0:
                continue
            else:
                dp[i] = dp[i-1] + i ** 2
    print(dp[n])
