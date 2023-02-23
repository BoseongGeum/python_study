n = int(input())
for x in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    r = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r1 >= r2:
        if r1 + r2 > r > r1 - r2:
            print(2)
        elif r > r1 + r2 or r < r1 - r2:
            print(0)
        elif r == r1 + r2 or r == r1 - r2:
            print(1)
    elif r2 > r1:
        if r1 + r2 > r > r2 - r1:
            print(2)
        elif r > r1 + r2 or r < r2 - r1:
            print(0)
        elif r == r1 + r2 or r == r2 - r1:
            print(1)
