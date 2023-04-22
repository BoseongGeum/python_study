import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if a + b + c  <= 2 * max(a, b, c):
    print((a + b + c - max(a, b, c)) * 2 - 1)
else:
    print(a + b + c)
