import sys
input = sys.stdin.readline

k = int(input())
a = 1
b = 0
for _ in range(k):
    temp = a
    a = b
    b += temp

print(a, b)
