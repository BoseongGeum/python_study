import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l = sorted(list(map(int, input().split())))
    if l[1] + 4 <= l[3]:
        print('KIN')
    else:
        print(sum(l[1:4]))
