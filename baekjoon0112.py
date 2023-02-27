import sys
input = sys.stdin.readline

n,m = map(int, input().split())
c = 0
l = [m, n-m]

i = 1
while True:
    if n < 5**i:
        break
    c += n // 5**i
    i += 1

for x in l:
    i = 1
    while True:
        if x < 5**i:
            break
        c -= x // 5**i
        i += 1
if n == 5:
    if m == 1 or 4:
        print(0)
else:
    print(c)
