n = int(input())

c = [[0] * n] * n

def strassen(i, j, n):

    if n == 2:
        for i in range(i, i + n):
            for j in range(j, j + n):
                for k in range(n):
                    c[i][j] += a[i][k] * b[k][j]

    while n != 2:
        stassen(i, j + n // 2, n // 2)
        stassen(i, j, n // 2)
        stassen(i + n // 2 , j + n // 2, n // 2)
        stassen(i + n // 2, j, n // 2)

    m1 = (a[i][j] + a[i+1][j+1]) * (b[i][j] + b[i+1][j+1])

print(c)
