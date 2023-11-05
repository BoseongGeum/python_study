import sys
input = sys.stdin.readline

minb = minc = 2000
for _ in range(3):
    b = int(input())
    if b < minb:
        minb = b
for _ in range(2):
    c = int(input())
    if c < minc:
        minc = c
print(minb + minc - 50)
    
