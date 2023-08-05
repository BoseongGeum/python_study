import sys
input = sys.stdin.readline

s = 0
for i in range(1, 4):
    s += i * int(input())

if s < 10:
    print('sad')
else:
    print('happy')
