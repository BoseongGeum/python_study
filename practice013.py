m = int(input())
n = int(input()) + 1

dp = [[0 for _ in range(n)] for _ in range(n)]
p = [[0 for _ in range(n)] for _ in range(n)]
d = [5, 2, 3, 4, 6, 7, 8]

for j in range(1, n):
    for i in reversed(range(1, j)):
        l = []
        for k in range(i, j):
            if dp[i][j] == 0:
                dp[i][j] = dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]
                p[i][j] = k
            else:
                if dp[i][j] > dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]:
                    dp[i][j] = dp[i][k] + dp[k+1][j] + d[i-1]*d[k]*d[j]
                    p[i][j] = k
            
print(dp[m][n-1])

s = ''
def seq(m, n):
    global s
    if n - m == 0:
        s += f'A{m}'
        return
    else:
        s += '('
        seq(m, p[m][n])
        seq(p[m][n]+1, n)
        s += ')'

seq(m, n-1)
print(s)
