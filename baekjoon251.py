import sys
input = sys.stdin.readline          

a = [[False for _ in range(101)] for _ in range(101)]
c = 0

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if a[i][j] == False:
                a[i][j] = True
                c += 1

print(c)
