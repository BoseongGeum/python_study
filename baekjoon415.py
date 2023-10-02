import sys
input = sys.stdin.readline

s = 0
n = int(input())

for i in range(1, n):
    s += n * i + i

print(s)
