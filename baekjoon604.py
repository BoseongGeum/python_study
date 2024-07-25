import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    sortedRanks = [0 for _ in range(n)]
    for _ in range(n):
        f, s = map(int, input().split())
        sortedRanks[f-1] = s

    passNum = 0
    minRank = float('inf')

    for rank in sortedRanks:
        if rank < minRank:
            passNum += 1
            minRank = rank

    print(passNum)
