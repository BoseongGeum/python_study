import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

i = 0
s = 0
for a in l:
    if a == 1:
        i += 1
        s += i
    else:
        i = 0

print(s)
