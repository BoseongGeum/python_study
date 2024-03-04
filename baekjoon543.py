import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, t+1):
    a, b, c = map(int, input().split())
    print(f'Case #{i}: ', end='')
    if max(a, b, c) * 2 - (a + b + c) >= 0:
        print('invalid!')
    elif a == b == c:
        print('equilateral')
    elif a == b or b == c or c == a:
        print('isosceles')
    else:
        print('scalene')
