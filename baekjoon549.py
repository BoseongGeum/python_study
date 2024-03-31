import sys
input = sys.stdin.readline

s = input().rstrip()
r = ''
i = 0
while i < len(s):
    r += s[i]
    if s[i] in ['a','e','i','o','u']:
        i += 2
    i += 1

print(r)
