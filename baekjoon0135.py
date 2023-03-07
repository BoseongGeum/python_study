import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [0]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    l[a:b+1] = [c]*(b-a+1)
del l[0]
print(*l)
