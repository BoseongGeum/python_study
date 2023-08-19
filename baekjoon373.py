import sys
input = sys.stdin.readline

nl = []
n = int(input())
l = list(map(int, input().split()))
for i in range(n):
    a = l[i] * (i+1) - sum(nl)
    nl.append(a)

print(*nl)
