import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    
    p1s = 0
    p2s = 0
    for _ in range(n):
        p1, p2 = input().split()
        if (p1 == 'R' and p2 == 'S') or (p1 == 'S' and p2 == 'P') or (p1 == 'P' and p2 == 'R'):
            p1s += 1
        elif (p2 == 'R' and p1 == 'S') or (p2 == 'S' and p1 == 'P') or (p2 == 'P' and p1 == 'R'):
            p2s += 1
            
    if p1s > p2s:
        print('Player 1')
    elif p2s > p1s:
        print('Player 2')
    else:
        print('TIE')
