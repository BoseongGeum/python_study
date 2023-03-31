n = int(input())
m = int(input())

w = [[0, 1, 100, 1, 5], [9, 0, 3, 2, 1], [100, 100, 0, 4, 100], [100, 100, 2, 0, 3], [3, 100, 100, 100, 0]]
d = w[:]
p = [[-1 for _ in range(5)] for _ in range(5)]

for k in range(5):
    for j in range(5):
        for i in range(5):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

print(d[n-1][m-1])
