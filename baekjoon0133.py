import sys
input = sys.stdin.readline

n = int(input())
cost = []
gap = 0
for _ in range(n):
    l = list(map(int, input().split()))
    cost.append(l)
cost_init = cost

for y in sorted(cost[0]):
    costsum = y
    color = cost[0].index(y)
    for x in cost[1:]:
        if color == x.index(min(x)):
            x[x.index(min(x))] = 1001
        costsum += min(x)
        color = x.index(min(x))
        x[x.index(min(x))] = min(cost_init(x))
    print(costsum)
