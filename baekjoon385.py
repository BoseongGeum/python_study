import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        print(a * 2 - b)
