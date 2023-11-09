import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    l = sorted(l[1:])
    print(f'Class {i+1}')
    maxv = max(l)
    minv = min(l)
    gap = 0
    for j in range(len(l)-1):
        if gap < l[j+1] - l[j]:
            gap = l[j+1] - l[j]
    print(f'Max {maxv}, Min {minv}, Largest gap {gap}')
