import sys
input = sys.stdin.readline          
    
n = int(input())

for i in range(n):
    if i % 2 == 0:
        print('* ' * (n - 1) + '*')
    else:
        print(' *' * n)
