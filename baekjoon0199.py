import sys
input = sys.stdin.readline

n = int(input())
b = n//2
s = 1

for x in range(n):
    print(' ' * b + '*' * s + ' ' * b)

    if s < n:
        b -= 1
        s += 2

    else:
        while s > 1:
            b += 1
            s -= 2
            print(' ' * b + '*' * s + ' ' * b)

        break
