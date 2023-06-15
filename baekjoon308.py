import sys
input = sys.stdin.readline

s = 91
for i in range(3):
    if i == 1:
        s += int(input()) * 3
    else:
        s += int(input())

print('The 1-3-sum is', s)
