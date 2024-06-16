import sys
from collections import deque, defaultdict
input = sys.stdin.readline

graph = defaultdict(list)

n, m, v = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfsVisited = {i:False for i in range(1, n+1)}
print(v, end='')

def dfs(node):
    dfsVisited[node] = True
    
    for new in graph[node]:
        if dfsVisited[new] == False:
            print(f' {new}', end='')
            dfs(new)
            
dfs(v)
print()

bfsVisited = {i:False for i in range(1, n+1)}
bfsRoute = []

queue = deque()
queue.append(v)
bfsVisited[v] = True

while queue:
    node = queue.popleft()
   
    for new in graph[node]:
        if bfsVisited[new] == False:
            queue.append(new)
            bfsVisited[new] = True
            
    bfsRoute.append(node)

print(*bfsRoute)
            
