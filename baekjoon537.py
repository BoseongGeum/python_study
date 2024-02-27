import sys
input = sys.stdin.readline
from collections import deque

sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

if es < ss:
    em -= 1
    es += 60
rs = es - ss

if em < sm:
    eh -= 1
    em += 60
rm = em - sm

if eh < sh:
    eh += 24
rh = eh - sh

print(f'{str(rh).zfill(2)}:{str(rm).zfill(2)}:{str(rs).zfill(2)}')
