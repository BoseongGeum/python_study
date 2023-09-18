import sys
input = sys.stdin.readline

l, r, a = map(int, input().split())

if (l >= r and l <= r + a) or (l < r and l + a >= r):
    print((l + r + a) // 2 * 2)

else:
    print((min(l, r) + a) * 2)
