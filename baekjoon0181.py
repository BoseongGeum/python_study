import sys
input = sys.stdin.readline

n = int(input())

l = []
for _ in range(n):
    a, b, c = map(int, input().split())
    
    if a == b == c:
        l.append(10000 + a * 1000)
    elif a == b or a == c:
        l.append(1000 + a * 100)
    elif b == c:
        l.append(1000 + b * 100)
    else:
        l.append(max(a, b, c) * 100)

print(max(l))
