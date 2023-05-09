import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
k = int(input())
r = list(map(int, input().split()))

if k >= n:
    print(0)

else:
    heapify(r)

    g = []
    a = heappop(r)
    i = a
    for _ in range(len(r)):
        b = heappop(r)
        heappush(g, a - b)
        a = b

    s = 0
    for _ in range(k - 1):
        s -= heappop(g)
        
    print(a - i - s)
