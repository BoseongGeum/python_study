import sys
input = sys.stdin.readline
import heapq as h

n = int(input())
l = [[] for _ in range(n+1)]
for _ in range(n):
    d, c = map(int, input().split())
    h.heappush(l[d], -c)

s = 0
for i in range(1, n+1)[::-1]:
    nl = []
    for j in range(i, n+1):
        if l[j] == []:
            continue
        h.heappush(nl, h.heappop(l[j]))
    if nl == []:
        continue
    s += -h.heappop(nl)

print(s)
