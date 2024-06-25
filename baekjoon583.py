import sys
input = sys.stdin.readline

n = int(input())
room = []
for _ in range(n):
    room.append(input().rstrip())

horCount = 0
verCount = 0

for i in range(n):
    space = 0
    for j in range(n):
        if room[i][j] == '.':
            space += 1
        if room[i][j] == 'X' or j == n-1:
            if space > 1:
                horCount += 1
            space = 0

for i in range(n):
    space = 0
    for j in range(n):
        if room[j][i] == '.':
            space += 1
        if room[j][i] == 'X' or j == n-1:
            if space > 1:
                verCount += 1
            space = 0

print(horCount, verCount)
