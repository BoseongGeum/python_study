import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n, m = map(int, input().split())
l1 = map(int, input().split())
l2 = [0]
s = 0
for x in l1:
    s += x
    l2.append(s)
for _ in range(m):
    a, b = map(int, input().split())
    print(l2[b] - l2[a - 1])
