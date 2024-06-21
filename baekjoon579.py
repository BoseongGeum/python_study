import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
isqueue = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))

queue = deque()
for i in range(n):
    if isqueue[i] == 0:
        queue.append(queuestack[i])
        
answer = []

for i in l:
    queue.appendleft(i)       
    answer.append(queue.pop())

print(*answer)
