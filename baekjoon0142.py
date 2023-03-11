import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [i for i in range(n+1)] 

for _ in range(m):
    a, b = map(int, input().split())
    c = l[b]
    l[b] = l[a]
    l[a] = c
    
print(*l[1:])
