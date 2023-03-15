import sys
input = sys.stdin.readline

n = int(input())

def point_star(n):
    
    if (i//n) % 3 == 1 and (j//n) % 3 == 1:
        print(' ', end='')

    elif n//3 == 0:
        print('*', end='')

    else:
        point_star(n//3)

for i in range(n):
    for j in range(n):
        point_star(n)
    print()
