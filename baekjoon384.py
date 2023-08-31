import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif a + c == b * 2:
        print('AP', c * 2 - b)
    else:
        print('GP', b // a * c)
