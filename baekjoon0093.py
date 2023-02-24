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
        if r > d1 or r > d2 :
            if r > d1 and r > d2:
                pass
            else:
                c += 1
    print(c)
