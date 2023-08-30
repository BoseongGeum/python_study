import sys
input = sys.stdin.readline

n1, n2, n3 = map(int, input().split())
order = input().rstrip()

l = sorted([n1, n2, n3])

pl = []
for a in order:
    if a == 'A':
        pl.append(l[0])
    elif a == 'B':
        pl.append(l[1])
    else:
        pl.append(l[2])

print(*pl)
