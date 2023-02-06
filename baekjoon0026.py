import sys

t = int(input())
l1 = []
l2 = []

for x in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    l1.append(a)
    l2.append(b)
    
for x in range(t):
    print(l1[x] + l2[x])
