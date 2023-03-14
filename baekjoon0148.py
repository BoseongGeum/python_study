import sys
input = sys.stdin.readline

n = int(input())
s_t = [list(map(int, input().split())) for _ in range(n)]
f_t = sorted([[y,x] for [x,y] in s_t])
c = 1
finish = f_t[0][0]

for x in range(1, n):
    if finish <= f_t[x][1]:
        c += 1
        finish = f_t[x][0]

print(c)
