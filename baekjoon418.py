import sys
input = sys.stdin.readline

n = int(input())
l = list(input().rstrip())

Adrian = ['A', 'B', 'C'] * 34
Bruno = ['B', 'A', 'B', 'C'] * 25
Goran = ['C', 'C', 'A', 'A', 'B', 'B'] * 17

ac = bc = gc = 0

for i in range(n):
    if Adrian[i] == l[i]:
        ac += 1
    if Bruno[i] == l[i]:
        bc += 1
    if Goran[i] == l[i]:
        gc += 1

maxi = max(ac, bc, gc)

print(maxi)
if ac == maxi:
    print('Adrian')
if bc == maxi:
    print('Bruno')
if gc == maxi:
    print('Goran')
