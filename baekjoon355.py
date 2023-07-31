import sys
input = sys.stdin.readline

s = 0
while True:
    i = int(input())
    if i == -1:
        break
    
    s += i

print(s)
