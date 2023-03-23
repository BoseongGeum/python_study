import sys
input = sys.stdin.readline

n = int(input())
l = [list(input().rstrip()) for _ in range(n)]

s = ''
def quadtree(i, j, n):
    global s
    
    for x in range(i, i + n):
        for y in range(j, j + n):
            if l[x][y] != l[i][j]:
                s += '('
                quadtree(i, j, n//2)
                quadtree(i, j + n//2, n//2)
                quadtree(i + n//2, j, n//2)
                quadtree(i + n//2, j + n//2, n//2)
                s += ')'
                return

    s += l[i][j]

quadtree(0, 0, n)
print(s)
