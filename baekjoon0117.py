import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) 

n = int(input())
xy_list = []
for x in range(n):
    for y in range(n):
        xy_list.append((x, y))
d = {k:False for k in xy_list} 
c1 = 0

def n_queen():
    global c1
    global d
    if c1 == n+1:
        print(d.values().count(False))
    for [x, y] in xy_list:
        for z in range(n):
            d[(x,z)] = True
            d[(z,y)] = True
        while True:
            x1 = x
            y1 = y
            if x1 == n - 1 or y1 == n - 1:
                break
            x1 += 1
            y1 += 1
            d[(x1,y1)] = True
        while True:
            x1 = x
            y1 = y
            if x1 == n - 1 or y1 == 0:
                break
            x1 += 1
            y1 -= 1
            d[(x1,y1)] = True
        while True:
            x1 = x
            y1 = y
            if x1 == 0 or y1 == n - 1:
                break
            x1 -= 1
            y1 += 1
            d[(x1,y1)] = True
        while True:
            x1 = x
            y1 = y
            if x1 == 0 or y1 == 0:
                break
            x1 -= 1
            y1 -= 1
            d[(x1,y1)] = True
        c1 += 1
        n_queen()
        d = {k:False for k in xy_list}

n_queen()
