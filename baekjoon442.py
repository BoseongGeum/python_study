import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in reversed(range(21)):
        if n >= 2 ** i:
            n -= 2 ** i
            l.append(i)
            
    print(*sorted(l))
