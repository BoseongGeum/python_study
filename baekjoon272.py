import sys
input = sys.stdin.readline

n = int(input())

s = 0
for i in range(n+1):
    for j in range(i, 2*i+1):
        s += j
        
print(s)
