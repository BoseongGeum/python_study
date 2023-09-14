import sys
input = sys.stdin.readline

uj = list(map(int, input().split()))
sg = list(map(int, input().split()))

uj_score = sg_score = 0
yes = False

for i in range(9):
    uj_score += uj[i]
    if uj_score > sg_score:
        yes = True
        break
    sg_score += sg[i]

if yes:
    print('Yes')
else:
    print('No')
