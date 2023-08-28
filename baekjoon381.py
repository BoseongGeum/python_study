import sys
input = sys.stdin.readline

r, c, zr, zc = map(int, input().split())
l = ['' for _ in range(r)]
for i in range(r):
    l[i] = input().rstrip()

for i in range(r):
    for _ in range(zr):
        for j in range(c):
            print(l[i][j] * zc, end='')
        print()
