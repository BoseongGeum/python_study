import sys
input = sys.stdin.readline

n, t = map(int, input().split())
l = list(map(int, input().split()))

s = -1
for i in range(n):
    if t < l[i]:
        s = i
        break
    t -= l[i]

if s == -1:
    print(n)
else:
    print(s)
