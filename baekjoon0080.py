import sys

n = int(input())
l = []
for x in range(n):
    w = sys.stdin.readline().rstrip()
    if [len(w), w] in l:
        continue
    l.append([len(w), w])
for x in sorted(l):
    print(x[1])
