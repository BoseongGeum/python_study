import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
c = 0
for i in l:
    if i == n:
        c += 1

print(c)
