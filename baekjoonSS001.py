import sys
input = sys.stdin.readline

n = int(input())
m = [[False] * n] * n
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
lotation = [input().split() for _ in range(l)]
now = [0, 0]
d = 'right'
t = 0

def start():
    m[0][0] = True
    for [x, y] in range(k):
        m[x - 1][y - 1] = 'a'
    
def move():
    if d = 'right':
        now[1] += 1
    elif d = 'left':
        now[1] -= 1
    elif d = 'up':
        now[0] -= 1
    elif d = 'down':
        now[0] += 1
    if m[now[0], now[1]] == True:
        finish()
    else:
        m[now[0], now[1]] = True
    t += 1

def finish():
