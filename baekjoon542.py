import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, unit = input().split()
    n = float(n)
    if unit == 'kg':
        print(f'{n * 2.2046:.4f} lb')
    elif unit == 'lb':
        print(f'{n * 0.4536:.4f} kg')
    elif unit == 'l':
        print(f'{n * 0.2642:.4f} g')
    else:
        print(f'{n * 3.7854:.4f} l')
