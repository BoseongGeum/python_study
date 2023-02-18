import sys

n = int(input())
l = []
for x in range(n):
    w = sys.stdin.readline().rstrip().split()
    l.append(w)
for x in sorted(l):
    print(x, sep='')
