import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [int(input()) for _ in range(n)]
cc = 0

for x in reversed(l):
    if (m // x) != 0:
        cc += m // x
        m %= x

print(cc)
