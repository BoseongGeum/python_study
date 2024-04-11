import sys
from string import ascii_uppercase
input = sys.stdin.readline

l = [' '] + list(ascii_uppercase)
d = {}
for i in range(len(l)):
    d[l[i]] = i

while True:
    s = input().rstrip()
    t = 0
    if s == '#':
        break
    for i in range(len(s)):
        t += d[s[i]] * (i + 1)
    print(t)
