import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):

    b = input().rstrip()

    while True:
        if not '()' in b:
            break
        
        b = b.replace('()', '')

    if b == '':
        print('YES')

    else:
        print('NO')
