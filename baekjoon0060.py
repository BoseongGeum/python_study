import sys

t = int(input())
for x in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    l = []
    for x in range(k):
        l.append(range(1, n))
    print(sum(l))
