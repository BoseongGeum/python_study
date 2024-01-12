import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if c == max(a, b, c):
    if a + b == c:
        fir = '+'
    else:
        fir = '*'
    sec = '='
elif a == max(a, b, c):
    if a - b == c:
        fir = '-'
    else:
        fir = '/'
    sec = '='
else:
    if a == b - c:
        sec = '-'
    else:
        sec = '/'
    fir = '='

print(f'{a}{fir}{b}{sec}{c}')
