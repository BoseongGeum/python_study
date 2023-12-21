import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    print(sum(l))
