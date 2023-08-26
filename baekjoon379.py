import sys
input = sys.stdin.readline

l = []
for i in range(8):
    l.append([int(input()), i+1])

l.sort()
nl = []
s = 0
for i in l[3:]:
    s += i[0]
    nl.append(i[1])

print(s)
print(*sorted(nl))
