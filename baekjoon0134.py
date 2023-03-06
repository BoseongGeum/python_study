import sys
input = sys.stdin.readline

l = []
n = int(input())
for _ in range(n):
    l.append(list(map(int, input().split())))
    
for a in range(1, n):
    l[a][0] += l[a-1][0]
    l[a][a] += l[a-1][a-1]
    for x in range(1, a):
        if l[a-1][x] > l[a-1][x-1]:
            l[a][x] += l[a-1][x]
        elif l[a-1][x] <= l[a-1][x-1]:
            l[a][x] += l[a-1][x-1]
print(max(l[n-1]))
