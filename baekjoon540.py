import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    c = [0] * (n+1)
    for i in range(1, n+1):
        c[i] = int(input())
    if c.count(max(c)) > 1:
        print('no winner')
    elif max(c) * 2 > sum(c):
        print('majority winner', c.index(max(c)))
    else:
        print('minority winner', c.index(max(c)))
