import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d, a, b, f = input().split()
    print(n, float(d)/(float(a)+float(b))*float(f))
