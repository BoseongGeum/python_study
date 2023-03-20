import sys
input = sys.stdin.readline

n = int(input())

def star(n):
    
    if (x//n) % 3 == 1 and (y//n) % 3 == 1:
        print(' ', end='')

    elif n // 3 == 0:
        print('*', end='')

    else:
        star(n//3)

for x in range(n):
    for y in range(n):
        star(n)

    print()
