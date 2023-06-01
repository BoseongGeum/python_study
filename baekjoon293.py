import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    o = input().rstrip()
    if o =='pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif o == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    else:
        p, m = o.split()
        q.append(m)
