import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    print(sorted(l)[7])
