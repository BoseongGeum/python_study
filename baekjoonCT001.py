import sys
input = sys.stdin.readline          

def createMap(n):
    m1 = [[[] for _ in range(n)] for _ in range(n)]
    return m1

def Is(x, y):
    return -1 < x < n and -1 < y < n and m2[x][y] != 2

def changeD(d):
    if d % 2 == 1:
        return d - 1
    else:
        return d + 1
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
pl = []

n, p = map(int, input().split())
m1 = createMap(n)
m2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(p):
    x, y, d = map(int, input().split())
    m1[x-1][y-1].append(i)
    pl.append([i, x-1, y-1, d-1])

turn = -1

for t in range(1000):
    c = False
    
    for i, x, y, d in pl:
        if m1[x][y][0] != i:
            continue
        X, Y = x + dx[d], y + dy[d]

        if not Is(X, Y):

            d = changeD(d)
            pl[i][3] = d
            X += 2 * dx[d]
            Y += 2 * dy[d]

            if not Is(X, Y):
                continue
            
        if m2[X][Y] == 1:
            m1[x][y].reverse()
            
        m1[X][Y] += m1[x][y]
        m1[x][y] = []

        for i in m1[X][Y]:
            pl[i][1] = X
            pl[i][2] = Y
            
        if len(m1[X][Y]) >= 4:
            c = True
            break
    if c:
        turn = t + 1
        break

print(turn)
