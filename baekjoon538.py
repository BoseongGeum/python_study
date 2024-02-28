import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    s = input().rstrip()
    print(f'String #{i}')
    for a in s:
        if a == 'Z':
            print('A', end='')
        else:
            print(chr(ord(a) + 1), end='')
    if i == n:
        print()
    else:
        print('\n')
