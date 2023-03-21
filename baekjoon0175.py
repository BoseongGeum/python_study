import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l = input().split()
    s = float(l[0])
    for x in l[1:]:
        if x == '@':
            s *= 3
        elif x == '%':
            s += 5
        else:
            s -= 7

    print('%.2f' % s)
