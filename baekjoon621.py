import sys
input = sys.stdin.readline
from string import ascii_lowercase


n = int(input())

for i in range(1, n+1):
    pangram = {a:0 for a in ascii_lowercase}

    msg = input().rstrip().lower()

    for c in msg:
        if 97 <= ord(c) <= 122:
            pangram[c] += 1

    count = min(pangram.values())

    if count >= 3:
        out = 'Triple pangram!!!'
        
    elif count == 2:
        out = 'Double pangram!!'
        
    elif count == 1:
        out = 'Pangram!'
        
    else:
        out = 'Not a pangram'

    print(f'Case {i}: {out}')
