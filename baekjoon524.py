import sys
input = sys.stdin.readline

big = [1, 3, 5, 7, 8, 10, 12]
small = [4, 6, 9, 11]

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    
    if 0 <= x < 24 and 0 <= y < 60:
        print('Yes ', end = '')
    else:
        print('No ', end = '')
        
    if x in big and 0 < y <= 31:
        print('Yes')
    elif x in small and 0 < y <= 30:
        print('Yes')
    elif x == 2 and 0 < y <= 29:
        print('Yes')
    else:
        print('No')
