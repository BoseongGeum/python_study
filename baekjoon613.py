import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) % 1500000

fibo = deque()

fibo.append(0)
fibo.append(1)

for _ in range(n):
    a = fibo.popleft()
    b = fibo.popleft()
    
    fibo.append(b)
    fibo.append((a+b)%1000000)

print(fibo.popleft())
