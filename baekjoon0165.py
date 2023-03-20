import sys
input = sys.stdin.readline
import collections

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n  = int(input())
    s = input()
    s = s[:-1].replace('[', '').replace(']' ,'')
    if s == '':
        l = []
    else:
        l = list(map(int, s.split(',')))

    if len(l) < p.count('D'):
        print('error')
        continue
    
    q = collections.deque(l)
    c = 0
    for x in p:
        if x == 'R':
            c += 1

        else:
            if len(q) == 0:
                break
            else:
                if c % 2 == 1:
                    q.pop()
                else:
                    q.popleft()

    
    if c % 2 == 1:
        print('[' + ','.join(s for s in
                            map(str, reversed(q))) + ']')
        
    else:
        print('[' + ','.join(s for s in map(str, q))
                  + ']')
