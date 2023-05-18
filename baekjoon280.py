import sys
input = sys.stdin.readline

join = [[] for _ in range(201)]

n = int(input())
for _ in range(n):
    i, name = input().split()
    join[int(i)].append(name)

for j in range(1, 201):
    for k in join[j]:
        print(j, k)
