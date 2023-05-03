import sys
input = sys.stdin.readline          

n = int(input())
f = list(map(int, input().split()))

c = 0
while True:
    sf = sorted(set(f))[::-1]
    m = sf[0]
    if len(sf) > 1:
        nm = sf[1]
        g = m - nm
    if m == 0:
        break
    i = f.index(m)
    if i < n - 2:
        if f[i+1] != 0 and f[i+2] != 0:
            minus = min(g, f[i+1], f[i+2])
            f[i] -= minus
            f[i+1] -= minus
            f[i+2] -= minus
            c += 7 * minus
        elif f[i+1] != 0 and f[i+2] == 0:
            minus = min(g, f[i+1])
            c += 5 * minus
            f[i] -= minus
            f[i+1] -= minus
        else:
            c += 3 * g
            f[i] = nm

    elif i == n - 2:
        if f[i+1] == 0:
            c += 3 * g
            f[i] = nm
        else:
            minus = min(g, f[i+1])
            c += 5 * minus
            f[i] -= minus
            f[i+1] -= minus

    else:
        c += 3 * g
        f[i] = nm

print(c)
