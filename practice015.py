n = 4
p = [0, 0.375, 0.375, 0.125, 0.125]
dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
r = [[0 for _ in range(n+2)] for _ in range(n+2)]

for j in range(1, n+1):
    for i in reversed(range(1, j+1)):
        l = []
        for k in range(i, j+1):
            if dp[i][j] == 0:
                dp[i][j] = dp[i][k-1] + dp[k+1][j] + sum(p[i:j+1])
                r[i][j] = k
            else:
                if dp[i][j] > dp[i][k-1] + dp[k+1][j] + sum(p[i:j+1]):
                    l.append(dp[i][k-1] + dp[k+1][j])
                    dp[i][j] = min(l) + sum(p[i:j+1])
                    r[i][j] = k

print(dp[1][n])

def tree(s, e):
    if s >= e:
        return
    else:
        tree(s, r[s][e] - 1)
        tree(r[s][e] + 1, e)

tree(1, n)
