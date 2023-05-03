import sys
input = sys.stdin.readline          

r, c = map(int, input().split())
m = [input().rstrip() for _ in range(r)]
n = int(input())
h = list(map(int, input().split()))

def isFall(x, y):
    if 'x' in [m[x-1][y], m[x+1][y], m[x][y-1], m[x][y+1]]:
        
    else:
        return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
for i in range(n):
    
    if i % 2 == 0:
        l = range(c)
    else:
        l = reversed(range(c))
        
    for j in l:
            if m[h[i]][j] == 'x':
                m[h[i]][j] == '.'
                x, y = h[i], j
                break
            
    if 
                
        
                
