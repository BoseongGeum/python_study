import sys
from heapq import *
input = sys.stdin.readline

n = int(input())

left_heap = [-int(input())]
right_heap = []

print(-left_heap[0])

for i in range(1, n):
    num = int(input())
    
    if i % 2 == 0:
        heappush(left_heap, -heappushpop(right_heap, num))
        
    else:
        heappush(right_heap, -heappushpop(left_heap, -num))

    print(-left_heap[0])
