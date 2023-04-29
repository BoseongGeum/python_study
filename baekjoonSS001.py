import sys
input = sys.stdin.readline

n = int(input())
m = [[False] * n] * n
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
rotation = [input().split() for _ in range(l)]

time = [int(x[0]) for x in rotation]
now = [0, 0]

right = 0
down = 1
left = 2
up = 3
d = right

t = 0

def start():
    m[0][0] = True
    for [x, y] in apple:
        m[x - 1][y - 1] = 'apple'
    move(d)
    
def move(d):
    global t
    i = 0
    while True:
        if t in time:
            if rotation[i][1] == 'D':
                d += 1
            else:
                d -= 1
            i += 1
                
        try:
            last = now
            t += 1
            if d % 4 == right:
                now[1] += 1
            elif d % 4 == left:
                now[1] -= 1
            elif d % 4 == up:
                now[0] -= 1
            elif d % 4 == down:
                now[0] += 1
                
            if m[now[0]][now[1]] == True:
                print(t)
                break
            elif m[now[0]][now[1]] == 'apple':
                m[now[0]][now[1]] = True
            else:
                m[now[0]][now[1]] = True
                m[last[0]][last[1]] = False
            
        except:
            print(t)
            break

def long():
    

start()
        
