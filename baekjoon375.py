import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    d = int(input())
    n = int(d ** 0.5)
    while n ** 2 + n > d:
        n -= 1

    print(n)
