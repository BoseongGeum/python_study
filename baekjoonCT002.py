import sys
input = sys.stdin.readline          

r, c = map(int, input().split())
m = [input().rstrip() for _ in range(r)]
n = int(input())
h = list(map(int, input().split()))

def neighbor(x, y):
    if 'x' in [m[x-1][y], m[x+1][y], m[x][y-1], m[x][y+1]]:
        return True
    else:
        return False
    
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
            
    if neighbor(x, y):
        n1 = neighbor(x-1, y)
        n2 = neighbor(x+1, y)
        n3 = neighbor(x, y-1)
        n4 = neighbor(x, y+1)

        for n in [n1, n2, n3, n4]:
            if not n:
                
