import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n = int(input())
xy_list = []
for x in range(n):
    for y in range(n):
        xy_list.append([x, y])
d = {k:False for k in xy_list} 
c1 = 0
c2 = 0

def n_queen():
    if c1 == 5:
        c2 += 
    for [x, y] in xy_list:
        for z in range(n):
            d[[x,z]] = True
            d[[z,y]] = True
        while True:
            if x1 == n - 1 or y1 == n - 1:
                break
            x1 = x
            y1 = y
            x1 += 1
            y1 += 1
            d[[x1,y1]] = True
        while True:
            if x1 == n - 1 or y1 == 0:
                break
            x1 = x
            y1 = y
            x1 += 1
            y1 -= 1
            d[[x1,y1]] = True
        while True:
            if x1 == 0 or y1 == n - 1:
                break
            x1 = x
            y1 = y
            x1 -= 1
            y1 += 1
            d[[x1,y1]] = True
        while True:
            if x1 == 0 or y1 == 0:
                break
            x1 -= 1
            y1 -= 1
            d[[x1,y1]] = True
        c1 += 1
        n_queen()
        
