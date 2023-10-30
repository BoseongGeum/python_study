import sys
input = sys.stdin.readline

i = 1
while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif i != 1:
        print()
    print(f'Triangle #{i}')
        
    if a == -1 and b < c:
        a = (c ** 2 - b ** 2) ** (1/2)
        print(f'a = {a:.3f}')
    elif b == -1 and a < c:
        b = (c ** 2 - a ** 2) ** (1/2)
        print(f'b = {b:.3f}')
    elif c == -1:
        c = (a ** 2 + b ** 2) ** (1/2)
        print(f'c = {c:.3f}')
    else:
        print('Impossible.')
    i += 1
