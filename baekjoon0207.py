import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    pm = 0
    sm = ''
    for _ in range(n):
        p, s = input().rstrip().split()
        p = int(p)
        
        if p > pm:
            pm = p
            sm = s

    print(sm)
