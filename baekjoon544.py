import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c, d = max(a, b), min(a, b)
    while d != 0:
        r = c % d
        c = d
        d = r
    print(a*b//c, c)
        
    
