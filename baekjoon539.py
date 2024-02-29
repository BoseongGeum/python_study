import sys
input = sys.stdin.readline

while True:
    n = sorted(list(map(int, input().split())))
    if n[0] == n[1] == n[2] == 0:
        break
    elif n[2] ** 2 == n[0] ** 2 + n[1] ** 2:
        print('right')
    else:
        print('wrong')
