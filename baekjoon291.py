import sys
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(1)
else:
    d = [0 for _ in range(n+1)]
    d[1] = 1
    d[2] = 3
    for i in range(3, n+1):
        d[i] = d[i-1] + 2 * d[i-2]

    print(d[n] % 10007)
