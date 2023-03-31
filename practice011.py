n = int(input())
m = int(input())

w = [[0, 1, 100, 1, 5], [9, 0, 3, 2, 100], [100, 100, 0, 4, 100], [100, 100, 2, 0, 3], [3, 100, 100, 100, 0]]
d = w[:]
p = [[-1 for _ in range(5)] for _ in range(5)]

for k in range(5):
    for j in range(5):
        for i in range(5):
            if d[i][j] > d[i][k] + d[k][j]:
                d[i][j] = d[i][k] + d[k][j]
                p[i][j] = k

print(d[n-1][m-1])

l = []

def path(n, m):
    if n+1 not in l:
        l.append(n+1)
    if p[n][m] == -1:
        return
    else:
        path(n, p[n][m])
        path(p[n][m], m)
        
path(n-1, m-1)    
print(*l, m)
