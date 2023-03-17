import sys
input = sys.stdin.readline
import collections

n = int(input())
q = collections.deque([])

for _ in range(n):

    l = input().split()
    
    if l[0] == 'push':
        q.append(int(l[1]))

    elif l[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif l[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])
            
    elif l[0] == 'size':
        print(len(q))

    elif l[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())

    elif l[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
