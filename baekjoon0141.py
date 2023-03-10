import sys
input = sys.stdin.readline

x = int(input())

if x <= 3:
    dp = [0, 0, 1, 1]

else:
    dp = [0]*(x+1)
    dp[2] = 1
    dp[3] = 1
    for z in range(4, x+1):

        if z % 3 == 0 and z % 2 == 0:
            dp[z] = min(dp[z//3], dp[z//2], dp[z-1]) + 1
            
        elif z % 3 == 0:
            dp[z] = min(dp[z//3], dp[z-1]) + 1
            
        elif z % 2 == 0:
            dp[z] = min(dp[z//2], dp[z-1]) + 1
            
        else:
            dp[z] = dp[z-1] + 1

print(dp[x])
