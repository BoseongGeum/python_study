from collections import deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    queue = deque([[0,0]])
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    
    
    while queue:
        print(maps)
        posx, posy = queue.pop()
        dis = maps[posx][posy]

        for dx, dy in directions:
            nx, ny = posx + dx, posy + dy
            
            if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1:
                queue.appendleft([nx, ny])
                maps[nx][ny] = dis + 1

            if nx == row - 1 and ny == col - 1:
                return maps[nx][ny]

    return -1
