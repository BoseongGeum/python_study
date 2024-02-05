import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d, n, s, p = map(int, input().split())
    if d > n * (s - p):
        print('do not parallelize')
    elif d < n * (s - p):
        print('parallelize')
    else:
        print('does not matter')
