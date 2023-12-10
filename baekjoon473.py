import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s = input().rstrip()

    for old in s:
        new = (a * (ord(old) - 65) + b) % 26
        print(chr(new + 65), end='')
    print()
