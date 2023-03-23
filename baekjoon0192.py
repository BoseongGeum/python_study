import sys
input = sys.stdin.readline

n = int(input())
sa = 100
sb = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        sb -= a
    elif a < b:
        sa -= b

print(sa, sb, sep='\n')
