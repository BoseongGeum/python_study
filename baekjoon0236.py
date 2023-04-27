import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d = map(int, input().split())
e = a * d + b * c
f = b * d
ar, br = e, f

while True:
    if ar == 0 or br == 0:
        break
    
    if ar > br:
        ar = ar % br
    else:
        br = br % ar

r = ar + br
print(e // r, f // r)
