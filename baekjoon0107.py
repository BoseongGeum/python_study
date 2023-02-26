import sys
input = sys.stdin.readline

n,m = map(int, input().split())
x1 = 1
x2 = 1
x3 = 1

for y in range(m+1, n+1):
    x1 *= y
    x2 *= x3
    x3 += 1
print(x1//x2)
