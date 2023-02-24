import sys
input = sys.stdin.readline

n = int(input())
f = set(map(int, input().split()))
if n == 1:
    print(max(f)**2)
else:
    print(max(f) * min(f))
