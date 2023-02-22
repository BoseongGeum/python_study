import sys

n, m = map(int, input().split())
s1 = set()
c = 0
for x in range(n):
    s1.add(sys.stdin.readline().rstrip())
for x in range(m):
    s2 = sys.stdin.readline().rstrip()
    if s2 in s1:
        c += 1

print(c)

