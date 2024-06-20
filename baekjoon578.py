import sys
input = sys.stdin.readline
from collections import deque

deq = deque()

n = int(input())

for _ in range(n):
    c = input().rstrip()
    
    if c[0] == '1':
        deq.append(c[2:])

    elif c[0] == '2':
        deq.appendleft(c[2:])
        
    elif c == '3':
        if not deq:
            print(-1)
        else:
            print(deq.pop())

    elif c == '4':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
            
    elif c == '5':
        print(len(deq))
        
    elif c == '6':
        if not deq:
            print(1)
        else:
            print(0)

    elif c == '7':
        if not deq:
            print(-1)
        else:
            print(deq[-1])

    elif c == '8':
        if not deq:
            print(-1)
        else:
            print(deq[0])
        
