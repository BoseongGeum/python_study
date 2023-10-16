import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    count = 0
    for b in range(1, n):
        for a in range(1, b):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                count += 1
    print(count)
