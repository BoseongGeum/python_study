import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    count = 0
    for _ in range(n):
        v, f, c = map(int,input().split())
        if d / v <= f / c:
            count += 1
    print(count)
