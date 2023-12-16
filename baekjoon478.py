import sys
input = sys.stdin.readline
from string import ascii_uppercase

n = int(input())
for _ in range(n):
    d = {k:0 for k in ascii_uppercase}
    s = input().rstrip()
    for c in s:
        if d[c] == 0:
            d[c] = 1
            
    total = 0
    for c in ascii_uppercase:
        if d[c] == 0:
            total += ord(c)
    print(total)
