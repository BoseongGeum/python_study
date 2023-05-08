import sys
import heapq as h

n = int(input())
heap = list(map(int, input().split()))
rheap = []
for i in heap:
    h.heappush(rheap, -i)

s = []
for j in range(n):
    a = h.heappop(heap)
    b = -h.heappop(rheap)
    h.heappush(s, a + b)

print(h.heappop(s))
