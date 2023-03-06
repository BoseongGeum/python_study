import sys
input = sys.stdin.readline

n = int(input())
cost = []
costsumlist = []
gap = 0
for _ in range(n):
    l = list(map(int, input().split()))
    cost.append(l)

for a in range(1, n):
    for x in range(3):
        if min(cost[a-1]) != cost[a-1][x]:
            cost[a][x] += min(cost[a-1])
        else:
            cost[a][x] += sorted(cost[a-1])[1]
            
print(min(cost[n-1]))
