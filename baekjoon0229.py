import sys
input = sys.stdin.readline

n, k = map(int, input().split())

i = 1
d = 1
while i < k:
    d += 1
    if d > n:
        break
    if n % d == 0:
        i += 1
        
if d > n:
    print(0)
else:
    print(d)
