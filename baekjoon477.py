import sys
input = sys.stdin.readline

n = int(input())
aCount = 0
bCount = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        aCount += 1
    elif b > a:
        bCount += 1

print(aCount, bCount)
