import sys
input = sys.stdin.readline

p = input().rstrip()
d = input().rstrip()

if len(p) > len(d):
    print('go')
else:
    print('no')
