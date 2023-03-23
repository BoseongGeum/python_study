import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

minus = zero = plus = 0

def paper(i, j, n):
    global minus, zero, plus
    
    for x in range(i, i + n):
        for y in range(j, j + n):
            if l[x][y] != l[i][j]:
                paper(i, j, n//3)
                paper(i, j + n//3, n//3)
                paper(i, j + 2 * n//3, n//3)
                paper(i + n//3, j, n//3)
                paper(i + n//3, j + n//3, n//3)
                paper(i + n//3, j + 2 * n//3, n//3)
                paper(i + 2 * n//3, j, n//3)
                paper(i + 2 * n//3, j + n//3, n//3)
                paper(i + 2 * n//3, j + 2 * n//3, n//3)
                return

    if l[i][j] == -1:
        minus += 1
    elif l[i][j] == 0:
        zero += 1
    else:
        plus += 1

paper(0, 0, n)
print(minus, zero, plus, sep='\n')
