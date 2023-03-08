import sys
input = sys.stdin.readline

x = 666
c = 0

n = int(input())

while True:
    if '666' in str(x):
        c += 1

    if n == c:
        print(x)
        break
    
    x += 1
