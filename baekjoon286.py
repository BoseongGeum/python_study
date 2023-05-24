import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

d = {}
sl = sorted(l)
i = 0
for x in sl:
    if x not in d:
        d[x] = i
        i += 1

for x in l:
    print(d[x], end=' ')
