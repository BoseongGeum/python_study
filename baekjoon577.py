import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
moves = list(map(int, input().split()))

ballons = []

for i, m in enumerate(moves):
    ballons.append([i+1, m])

ballons = deque(ballons)
result = []

while ballons:
    ballon, move = ballons.popleft()
    result.append(ballon)
    if move > 0:
        ballons.rotate(1-move)
    else:
        ballons.rotate(-move)

print(*result)
