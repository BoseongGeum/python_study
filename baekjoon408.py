import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    name = input().rstrip()

    good = 0
    bad = 0
    for a in name:
        if a == 'g' or a == 'G':
            good += 1
        elif a == 'b' or a == 'B':
            bad += 1

    if good > bad:
        side = 'GOOD'
    elif bad > good:
        side = 'A BADDY'
    else:
        side = 'NEUTRAL'

    print(f'{name} is {side}')
