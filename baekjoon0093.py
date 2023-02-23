import sys
input = sys.stdin.readline


t = int(input())
for x in range(t):
    c = 0
    x1,y1,x2,y2 = map(int, input().split())
    n = int(input())
    for x in range(n):
        cx,cy,r = map(int, input().split())
        d1 = ((cx-x1)**2+(cy-y1)**2)**(1/2)
        d2 = ((cx-x2)**2+(cy-y2)**2)**(1/2)
        d3 = ((x1-x2)**2+(y1-y2)**2)**(1/2)
        if d3 > r > d1 or d3 > r > d2:
            c += 1
    print(c)
