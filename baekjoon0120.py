import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n, m = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = []
l3 = []
s = 0
num = 1
for x in l1:
    if len(l2) >= m:
        s += x
        l2.append(s)
        l3.append(l2[-1] - l2[-1 - m])
    else:
        s += x
        l2.append(s)
        l3.append(s)
del l3[0:m - 1]
print(max(l3))
