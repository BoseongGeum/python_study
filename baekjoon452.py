import sys
input = sys.stdin.readline

s = input().rstrip()
for a in s:
    if 65 <= ord(a) <= 90:
        if ord(a) + 13 > 90:
            print(chr(ord(a) - 13), end='')
        else:
            print(chr(ord(a) + 13), end='')
    elif 97 <= ord(a) <= 122:
        if ord(a) + 13 > 122:
            print(chr(ord(a) - 13), end='')
        else:
            print(chr(ord(a) + 13), end='')
    else:
        print(a, end='')
