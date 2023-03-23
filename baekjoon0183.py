import sys
input = sys.stdin.readline

s = input().rstrip()

h = 10
for x in range(1, len(s)):
    if s[x] == s[x-1]:
        h += 5
    else:
        h += 10

print(h)
