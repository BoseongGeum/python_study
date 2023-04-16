import sys
input = sys.stdin.readline

n = int(input())
i = 2

for _ in range(n):
    i = i * 2 - 1

print(i ** 2)
