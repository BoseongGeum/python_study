import sys
input = sys.stdin.readline
from string import ascii_lowercase

dic = {k:0 for k in ascii_lowercase}

while True:
    s = input().rstrip()
    if s == '#':
        break
    for c in s:
        c = c.lower()
        if c in dic:
            dic[c] = 1
    print(sum(dic.values()))
    for a in dic:
        dic[a] = 0
