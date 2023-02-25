import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
xi = l[0]

for yi in l[1:]:
    y = yi
    x = xi
    while True:
        if x >= y:
            x = x % y
            if x == 0:
                print(f'{xi//y}/{yi//y}')
                break
        else:
            y = y % x
            if y == 0:
                print(f'{xi//x}/{yi//x}')
                break
