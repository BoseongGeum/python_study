import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
card = []
for _ in range(n):
    heappush(card, int(input()))
    
s = 0
while len(card) > 1:
    a = heappop(card)
    b = heappop(card)
    c = a + b
    heappush(card, c)
    s += c
    
print(s)
