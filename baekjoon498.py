import sys
input = sys.stdin.readline

t, a, b = map(int, input().split())
c = (a ** 2 + b ** 2) ** (1/2)

for _ in range(t):
    n = int(input())
    if n <= c:
        print('DA')
    else:
        print('NE')
