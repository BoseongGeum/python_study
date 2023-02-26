import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int, input().split())

    x = 1
    a = x
    l = []

    for y in range(1, m+1):
        x *= y
        if y == n or y == m - n:
            if n == m - n:
                l.append(x)
            l.append(x)
    for y in l:
        a *= y
    print(x//a)
