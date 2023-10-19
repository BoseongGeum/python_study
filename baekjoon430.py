import sys
input = sys.stdin.readline

maxi = c = 0
for _ in range(10):
    o, i = map(int, input().split())
    c += i - o
    if maxi < c:
        maxi = c
        
print(maxi)
