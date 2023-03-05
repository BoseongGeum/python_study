import sys
input = sys.stdin.readline

def tile(n):
    t[1] = 1
    t[2] = 2
    for x in range(3, n+1):
        t[x] = (t[x-2] + t[x-1]) % 15746
    return print(t[n])

n = int(input())
t = [0]*(n+2)
tile(n)
