from collections import deque

def solution(maps):
    n = len(maps[0])
    m = len(maps)
    queue = deque([[0,0,1]])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    while queue:
        posx, posy, dis = queue.pop()
        
        if maps[posx][posy] != 1 or visited[posx][posy] == True:
            continue
        
        if posx+1 < n:
            queue.appendleft([posx+1, posy, dis+1])
        if posy+1 < m:
            queue.appendleft([posx, posy+1, dis+1])
        if 0 < posx:
            queue.appendleft([posx-1, posy, dis+1])
        if 0 < posy:
            queue.appendleft([posx, posy-1, dis+1])
        
        maps[posx][posy] = dis
        visited[posx][posy] = True
            
    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]

print(solution([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))
