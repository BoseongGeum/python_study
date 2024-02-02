import sys
input = sys.stdin.readline

x = input().rstrip()
if x[0] != '0':
    print(x)
elif x[1] != 'x':
    print(int(x, 8))
else:
    print(int(x, 16))
