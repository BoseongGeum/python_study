import sys
input = sys.stdin.readline          

def createMap(n):
    m1 = [[[] for _ in range(n)] for _ in range(n)]
    return m1

def is(x, y):
    return -1 < x < n and -1 < y < n
    
def play():

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
pl = []

    n, p = map(int, input().split())
    m1 = createMap(n)
    m2 = [list(map(int, input().split())) for _ in range(n)]

    for i in range(p):
        x, y, d = map(int, input().split())
        m1[x-1][y-1].append(i)
        pl.append([i, x-1, y-1, d-1])
    
    while True:
        for i, x, y, d in pl:
            if m1[x][y][0] != i:
                continue
            X, Y = x + dx[d], y + dy[d]

            if is(X, Y):
            
                if m1[X][Y] == 0:
                    m1[X][Y] += m1[x][y]
                    m1[x][y] = []

                elif m1[X][Y] == 1:
                    
