n = int(input())
k = int(input())
b = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(min(i+1, k+1)):
            
        if j == 0 or j == i:
            b[i][j] = 1
            
        else:
            b[i][j] = b[i-1][j-1] + b[i-1][j]

print(b[n][k])
