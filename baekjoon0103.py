import sys
input = sys.stdin.readline
f = 1
nf,mf = map(int, input().split())
n = nf
m = mf
c = 2
while True:
    if n % c == 0 and m % c == 0:
        f *= c
        n = n / c
        m = m / c
    elif c > n or c > m:
        break
    else:
        c += 1
print(f)
print(int(nf*mf/f))
