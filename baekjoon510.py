import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

Atotal = a * e
if e > c:
    Btotal = b + (e - c) * d
else:
    Btotal = b

if Atotal > Btotal:
    print(Btotal)
else:
    print(Atotal)
