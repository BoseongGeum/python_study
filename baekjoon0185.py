import sys
input = sys.stdin.readline

n = int(input())

c1 = 0
c0 = 0
for _ in range(n):
    if int(input()) == 1:
        c1 += 1
    else:
        c0 += 1

if c1 > c0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
    
