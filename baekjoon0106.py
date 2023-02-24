import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

for x in l[1:]:
    y = l[0] / x
    m = 1
    while True:
        if y == int(y):
            break
        y *= m
        m += 1
    print(f'{int(y)}/{m}')
