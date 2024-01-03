import sys
input = sys.stdin.readline
from string import ascii_lowercase

initials = {k:0 for k in ascii_lowercase}
n = int(input())
for _ in range(n):
    name = input().rstrip()
    initials[name[0]] += 1

predaja = True
for i in list(initials.keys()):
    if initials[i] >= 5:
        predaja = False
        print(i, end='')

if predaja:
    print('PREDAJA', end='')
print()
