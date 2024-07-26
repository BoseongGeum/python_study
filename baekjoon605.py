import sys
input = sys.stdin.readline

n, newScore, p = map(int, input().split())

if n == 0:
    print(1)
    
else:
    scores = list(map(int, input().split()))

    rank = 0
    
    for score in scores:
        if newScore < score:
            rank += 1

    if n == p and newScore <= scores[-1]:
        print(-1)
        
    else:
        print(rank+1)
