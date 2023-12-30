import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a % b == 0:
        print(a // b)
    else:
        print(a // b + 1)
