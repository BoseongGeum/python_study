import sys
input = sys.stdin.readline

s = input().rstrip()

for a in s:
    if a.isupper():
        r = a.lower()
    else:
        r = a.upper()
    print(r, end='')
print()
