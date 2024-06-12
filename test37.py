from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0 for _ in range(25)] for _ in range(25)]
    for rec in rectangle:
        for x in range(rec[0]*2, rec[2]*2+1):
            for y in range(rec[1]*2, rec[3]*2+1):
                if maps[x][y] == 0:
                    maps[x][y] = 1
        for x in range(rec[0]*2+1, rec[2]*2):
            for y in range(rec[1]*2+1, rec[3]*2):
                maps[x][y] = -1

    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    
    queue = deque()
    queue.append([characterX*2, characterY*2])
    
    while queue:
        posX, posY = queue.popleft()
        dis = maps[posX][posY]
        
        for dX, dY in directions:
            nX, nY = posX + dX, posY + dY
            
            if maps[nX][nY] == 1:
                queue.append([nX, nY])
                maps[nX][nY] = dis+1
                
            if nX == itemX*2 and nY == itemY*2:
                return (maps[itemX*2][itemY*2]-1)//2

print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
