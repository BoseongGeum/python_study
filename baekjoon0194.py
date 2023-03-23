import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    L = []
    
    for _ in range(n):
        s, l = input().split()
        L.append([int(l), s])

    print(max(L)[1])
