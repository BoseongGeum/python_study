import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

l = sorted([a, b, c, d])
s1 = l[1] + l[2] + l[3]
s2 = max(e, f)

print(s1 + s2)
