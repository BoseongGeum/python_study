import sys
input = sys.stdin.readline

total = 0

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    total += b % a

print(total)
