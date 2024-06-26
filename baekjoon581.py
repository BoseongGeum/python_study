import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = max([dp[j]+p[i-j] for j in range(i+1)])

print(dp[n])
