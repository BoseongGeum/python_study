import sys
input = sys.stdin.readline

while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0:
        break
    elif n > m and n % m == 0:
        print('multiple')
    elif n < m and m % n == 0:
        print('factor')
    else:
        print('neither')