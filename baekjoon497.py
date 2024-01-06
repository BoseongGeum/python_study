import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = input().rstrip()
    i = len(n) // 2
    if n[i] == n[i-1]:
        print('Do-it')
    else:
        print('Do-it-Not')
