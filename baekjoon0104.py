import sys
input = sys.stdin.readline

t = int(input())
for x in range(t):
    ni,mi = map(int, input().split())
    n = ni
    m = mi
    while True:
        if n >= m:
            n = n % m
            if n == 0:
                print(int(ni*mi/m))
                break
        else:
            m = m % n
            if m == 0:
                print(int(ni*mi/n))
                break
