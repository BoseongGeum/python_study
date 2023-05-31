import sys
input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n == 3:
        print(4)
    else:
        d = [0 for _ in range(n+1)]
        d[1] = 1
        d[2] = 2
        d[3] = 4
        for i in range(4, n+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]

        print(d[n])
