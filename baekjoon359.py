import sys
input = sys.stdin.readline

n = int(input())

s = 1
for i in range(1, n+1):
    s *= i
print(s)
