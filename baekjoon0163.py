import sys
input = sys.stdin.readline
import collections

n = int(input())

d = collections.deque([])

for _ in range(n):
    o = input().split()

    if o[0] == 'push_back':
        d.append(o[1])

    elif o[0] == 'push_front':
        d.appendleft(o[1])

    elif o[0] == 'pop_back':
        if not d:
            print(-1)
        else:
            print(d.pop())
            
    elif o[0] == 'pop_front':
        if not d:
            print(-1)
        else:
            print(d.popleft())

    elif o[0] == 'size':
        print(len(d))

    elif o[0] == 'empty':
        if not d:
            print(1)
        else:
            print(0)

    elif o[0] == 'front':
        if not d:
            print(-1)
        else:
            print(d[0])

    elif o[0] == 'back':
        if not d:
            print(-1)
        else:
            print(d[-1])
