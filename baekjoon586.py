import sys
input = sys.stdin.readline

n, k = map(int, input().split())
countries = [[0,0,0] for _ in range(n+1)]

for _ in range(n):
    i, g, s, b = map(int, input().split())
    countries[i] = [g, s, b]

rank = 1

for c in countries:
    if countries[k][0] < c[0]:
        rank += 1
    elif countries[k][0] == c[0]:
        if countries[k][1] < c[1]:
            rank += 1
        elif countries[k][1] == c[1]:
            if countries[k][2] < c[2]:
                rank += 1

print(rank)
