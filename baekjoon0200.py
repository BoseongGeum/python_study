import sys
input = sys.stdin.readline

l = [0] * 5
for x in range(5):
    l[x] = input().rstrip()

for x in range(15):
    for y in range(5):
        if len(l[y]) > x:
            print(l[y][x], end='')
