import sys
input = sys.stdin.readline

l = []
for _ in range(2):
    a, b, c, d = map(int, input().split())
    l.append(a+b+c+d)

print(max(l))
