import sys
input = sys.stdin.readline

l = ['a', 'e', 'i', 'o', 'u']

s = input().rstrip()
c = 0

for i in range(len(s)):
    if s[i] in l:
        c += 1

print(c)
