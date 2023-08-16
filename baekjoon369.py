import sys
input = sys.stdin.readline

s = int(input())
tc = 0

while s > 0:
    c = 0
    
    while c < s:
        c += 1
        s -= c
        tc += 1

print(tc)
