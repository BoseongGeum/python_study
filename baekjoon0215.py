import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tp = 0
    ts = 0
    
    for _ in range(n):
        p, s = map(float, input().split())
        tp += p
        ts += s * p

    print(int(tp), '%.1f' % (ts/tp))
