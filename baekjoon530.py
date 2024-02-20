import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    x, o, y, e, z = input().split()
    if o == '+' and int(x) + int(y) == int(z):
        print(f'Case {i}: YES')
    elif o == '-' and int(x) - int(y) == int(z):
        print(f'Case {i}: YES')
    else:
        print(f'Case {i}: NO')
