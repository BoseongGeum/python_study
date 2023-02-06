import sys

t = True
l = []
x = 0

while t:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    l.append(a + b)
    if str(x) == str(l[-1]):
            t = False
for x in l:
    print(x)
