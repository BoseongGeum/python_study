import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    t, s = input().split()
    print(s * int(t))
