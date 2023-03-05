import sys
input = sys.stdin.readline

def padoban(n):
    for x in range(1, 4):
        p[x] = 1
    for x in range(4, 6):
        p[x] = 2
    for x in range(6, n+1):
        p[x] = p[x-5] + p[x-1]
    return print(p[n])

t = int(input())
m = []
for _ in range(t):
    m.append(int(input()))
p = [0]*(max(m)+1)
for x in m:
    padoban(x)
