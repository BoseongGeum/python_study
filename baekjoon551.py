import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n1, n2 = map(int, input().split())
    n = a = max(n1, n2)
    m = b = min(n1, n2)
    while b != 0:
        r = a % b
        a = b
        b = r
    print(n * m // a)
