import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
cList = sorted(input().split())

vow = ['a', 'e', 'i', 'o', 'u']

for password in combinations(cList, l):

    vowCount = 0
    for p in password:
        if p in vow:
            vowCount += 1

    if vowCount >= 1 and l - vowCount >= 2:
        print(''.join(password))
