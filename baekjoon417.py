import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

maxi = l[0]
mini = l[0]
gap = 0
for i in range(1, n):
    if l[i] > l[i-1]:
        maxi = l[i]
        if gap < maxi - mini:
            gap = maxi - mini
    else:
        mini = l[i]
        maxi = l[i]

print(gap)
