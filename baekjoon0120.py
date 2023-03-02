import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n, m = map(int, input().split())
l1 = map(int, input().split())
l2 = []
s = 0
for x in l1:
    s += x
    l2.append(s)
