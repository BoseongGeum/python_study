import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
cards = deque([i for i in range(1, n+1)])
while cards != []:
    print(cards.popleft(), end='')
    cards.rotate(-1)
    if cards != deque():
        print(' ', end='')
    else:
        break
