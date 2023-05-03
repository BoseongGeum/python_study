import sys
input = sys.stdin.readline          

n = int(input())
f = list(map(int, input().split()))

c = 0
for i in range(n - 2):
    if f[i] != 0 and f[i+1] != 0 and f[i+2] != 0:
            m = min(f[i], f[i+1], f[i+2])
            f[i] -= m
            f[i+1] -= m
            f[i+2] -= m
            c += m * 7

    if f[i] != 0 and f[i+1] != 0:
        m = min(f[i], f[i+1])
        f[i] -= m
        f[i+1] -= m
        c += m * 5
        
    if f[i] != 0:
        c += f[i] * 3

m = min(f[n-2], f[n-1])
if m == f[n-2]:
    f[n-1] -= m
    c += m * 5 + f[n-1] * 3

else:
    f[n-2] -= m
    c += m * 5 + f[n-2] * 3
    
print(c)
