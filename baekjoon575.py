import sys
input = sys.stdin.readline

lines = ['WBWBWBWB', 'BWBWBWBW']
maps = []

n, m = map(int, input().split())

for _ in range(n):
    maps.append(input().rstrip())

def counting(part):
    count = 0

    if part[0][0] == 'W':
        line = 0
    else:
        line = 1
    
    for i in range(8):
        for j in range(8):
            if part[i][j] != lines[line][j]:
                count += 1

        if line == 0:
            line = 1
        else:
            line = 0

    if count > 32:
        count = 64 - count

    return count

def makePart(i, j):
    part = []

    for l in range(i, i+8):
        part.append(maps[l][j:j+8])

    return part

answer = 32

for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, counting(makePart(i, j)))

print(answer)
