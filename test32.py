def solution(money):
    answer = 0
    dp = [0 for _ in range(len(money))]
    dp2 = dp[::]
    dp[0] = money[0]
    dp[1] = max(dp[0], money[1])
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    dp[-1] = dp[-2]
    
    dp2[0] = money[-1]
    dp2[1] = max(dp2[0], money[0])
    for i in range(2, len(money)-1):
        dp2[i] = max(dp2[i-2]+money[i-1], dp2[i-1])
    dp2[-1] = dp2[-2]
    
    return max(dp[-1], dp2[-1])
