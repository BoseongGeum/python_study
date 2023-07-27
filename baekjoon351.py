import sys
input = sys.stdin.readline

n = int(input())
c = int(input())
for i in range(n-1):
    v = int(input())
    if c < v:
        print('N')
        break
    elif i == n-2:
        print('S')
