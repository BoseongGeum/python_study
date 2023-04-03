import sys
input = sys.stdin.readline

n = int(input())
b = []

for i in range(n):
    name, d, m, y = input().split()
    b.append([int(y), int(m), int(d), name])

print(max(b)[3])
print(min(b)[3])
