import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ar, br = a, b

while True:
    if ar == 0 or br == 0:
        break
    
    if ar > br:
        ar = ar % br
    else:
        br = br % ar

c = ar + br
print(a * b // c)
