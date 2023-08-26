import sys
input = sys.stdin.readline

s = 0
for i in range(5):
    t = sum(list(map(int, input().split())))
    if s < t:
        s = t
        n = i + 1

print(n, s)
