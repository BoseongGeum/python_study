from collections import deque, defaultdict

def solution(n, edge):
    
    nodes = defaultdict(list)
    for a, b in edge:
        nodes[a].append(b)
        nodes[b].append(a)
    
    visited = {i:0 for i in range(1, n+1)}
    queue = deque()
    
    visited[1] = -1
    queue.append((1, 0))
    
    while queue:
        node, length = queue.pop()
        
        for dest in nodes[node]:
            if visited[dest] == 0:
                queue.appendleft((dest, length+1))
                visited[dest] = length+1
                
    count = 0
    maxLen = max(visited.values())
    for v in visited.values():
        if maxLen == v:
            count += 1
        
    return count

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
