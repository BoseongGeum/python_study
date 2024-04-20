import sys
input = sys.stdin.readline

sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

if es < ss:
    em -= 1
    es += 60
ws = es - ss

if em < sm:
    eh -= 1
    em += 60
wm = em - sm

if eh < sh:
    eh += 24
wh = eh - sh

if es == ss and em == sm and eh == sh:
    print('24:00:00')
else:
    print(f'{str(wh):0>2}:{str(wm):0>2}:{str(ws):0>2}')
