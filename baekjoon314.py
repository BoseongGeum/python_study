import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    i = (n // 2) + 1
    print(i ** 2)
