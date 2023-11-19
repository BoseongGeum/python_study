import sys
input = sys.stdin.readline

l = []
s = input().rstrip()
for i in range(len(s)):
    l.append(s[i:])

for p in sorted(l):
    print(p)
