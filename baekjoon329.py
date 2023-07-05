import sys
input = sys.stdin.readline

c = 0
for _ in range(6):
    r = input().rstrip()
    if r == 'W':
        c += 1

if c == 5 or c == 6:
    print(1)
elif c == 3 or c == 4:
    print(2)
elif c == 1 or c == 2:
    print(3)
else:
    print(-1)
