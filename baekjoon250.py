import sys
input = sys.stdin.readline          
    
n = int(input())

for i in range(n):
    l = ['*'] * (i + 1)
    print(' ' * (n - i - 1), end='')
    print(*l)
