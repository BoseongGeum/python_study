import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print((max(d) - min(d)) * 2)
