import sys
input = sys.stdin.readline

for _ in range(3):
    n = list(map(int, input().split()))
    s = sum(n)
    if s == 3:
        print('A')
    elif s == 2:
        print('B')
    elif s == 1:
        print('C')
    elif s == 0:
        print('D')
    else:
        print('E')
