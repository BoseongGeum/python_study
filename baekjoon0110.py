import sys
input = sys.stdin.readline
import collections

t = int(input())

for _ in range(t):
    n = int(input())
    l = []
    for _ in range(n):
        name, kind = input().split()
        l.append(kind)
    d = dict(collections.Counter(l))
    c = 1
    for x in d.values():
        c *= x+1
    print(c - 1)
