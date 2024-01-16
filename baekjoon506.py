import sys
input = sys.stdin.readline

l = [1, 1, 2, 4] + [0] * 64
t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(l[n])
    else:
        for i in range(4, n+1):
            l[i] = l[i-4] + l[i-3] + l[i-2] + l[i-1]
        print(l[n])
