import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10000)

graph = defaultdict(list)

n, m = map(int, input().split())
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = {i:False for i in range(1, n+1)}
count = 0

def dfs(node):
    
    visited[node] = True
    
    for nextNode in graph[node]:
        if visited[nextNode] == False:
            dfs(nextNode)
    

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
