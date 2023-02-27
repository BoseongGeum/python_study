import sys
input = sys.stdin.readline

n,m = map(int, input().split())
c1 = 0
c2 = 0
l = [m, n-m]

i = 1
while True:
    if n < 2**i:
        break
    c1 += n // 5**i
    c2 += n // 2**i
    i += 1

for x in l:
    i = 1
    while True:
        if x < 2**i:
            break
        c1 -= x // 5**i
        c2 -= x // 2**i
        i += 1

if c1 > c2:
    print(c2)
else:
    print(c1)
