import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10000)

graph = defaultdict(list)

n = int(input())
m = int(input())

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = {i:False for i in range(1, n+1)}
count = 0

def dfs(node):
    global count
    
    visited[node] = True
    
    for nextNode in graph[node]:
        if visited[nextNode] == False:
            dfs(nextNode)
            count += 1

dfs(1)
print(count)
