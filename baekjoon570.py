import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()

    if n == '0':
        break
    else:
        n, p1 = map(int, n.split())

    if p1 % 2 == 0:
        p2 = p1 - 1
    else:
        p2 = p1 + 1
        
    print(*sorted([p2, n - p1 + 1, n - p2 + 1]))
