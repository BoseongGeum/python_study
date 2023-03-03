import sys
import string
input = sys.stdin.readline

s = input().rstrip()
q = int(input())
d = {k:0 for k in string.ascii_lowercase}
for _ in range(q):
    c = 0
    clist = [0]
    a, l, r = input().split()
    if d[a] == 0:
        for x in s:
            if x == a:
                c += 1
            clist.append(c)
        d[a] = clist
    print(d[a][int(r)+1] - d[a][int(l)])
