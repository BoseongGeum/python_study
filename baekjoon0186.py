import sys
input = sys.stdin.readline

n = int(input())
v = input().rstrip()

cA = 0
cB = 0
for x in range(n):
    if v[x] == 'A':
        cA += 1
    else:
        cB += 1

if cA > cB:
    print('A')
elif cA == cB:
    print('Tie')
else:
    print('B')
