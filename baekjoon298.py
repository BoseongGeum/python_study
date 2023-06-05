import sys
input = sys.stdin.readline

n = input().rstrip()

s = 0
length = len(n) - 1

for i in n:
    if i == 'A':
        i = 10
    elif i == 'B':
        i = 11
    elif i == 'C':
        i = 12
    elif i == 'D':
        i = 13
    elif i == 'E':
        i = 14
    elif i == 'F':
        i = 15
    else:
        i = int(i)

    s += i * (16 ** length)
    length -= 1

print(s)
