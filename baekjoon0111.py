import sys
input = sys.stdin.readline

n = int(input())

x = 1
c = 0
for y in range(1, n+1):
    x *= y
l = reversed(list(str(x)))
for x in l:
    if x != '0':
        break
    c += 1
print(c)
