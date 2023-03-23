import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

blue = white = 0
def paper(x, y, n):
    global blue, white
    color = l[x][y]
    for a in range(x, x+n):
        for b in range(y, y+n):
            if l[a][b] != color:
                paper(x, y, n//2)
                paper(x+n//2, y, n//2)
                paper(x, y+n//2, n//2)
                paper(x+n//2, y+n, n//2)
                
    if color == 1:
        blue += 1
    else:
        white += 1

paper(0,0,n)
print(white)
print(blue)
