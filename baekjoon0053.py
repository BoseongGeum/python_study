import sys
import string

y = 3
di = {}
al = list(sys.stdin.readline().rstrip())
for x in string.ascii_uppercase:
    if x in ['D', 'G', 'J', 'M', 'P', 'T', 'W']:
        y += 1
    di[x] = y

s = 0
for x in al:
    s += di[x]
print(s)
