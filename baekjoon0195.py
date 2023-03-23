import sys
input = sys.stdin.readline

n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

white = blue = 0

def paper(a, b, n):
    global white, blue
    color = l[a][b]
    
    for x in range(a, a + n):
        for y in range(b, b + n):
            if l[x][y] != color:
                paper(a, b, n//2)
                paper(a + n//2, b, n//2)
                paper(a, b + n//2, n//2)
                paper(a + n//2, b + n//2, n//2)
                return

    if color == 1:
        blue += 1
    else:
        white += 1

paper(0, 0, n)
print(white, blue, sep='\n')
