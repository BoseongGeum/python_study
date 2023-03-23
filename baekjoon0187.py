import sys
input = sys.stdin.readline

f = input().rstrip()
f1 = list(reversed(f))
t = True

for x in range(len(f)):
    if f[x] != f1[x]:
        t = False
        break

if t == False:
    print(0)
else:
    print(1)
