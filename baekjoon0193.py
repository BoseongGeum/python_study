import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ys = 0
    ks = 0
    
    for _ in range(9):
        y, k = map(int, input().split())
        
        ys += y
        ks += k
        
    if ys > ks:
        print('Yonsei')
    elif ys < ks:
        print('Korea')
    else:
        print('Draw')
