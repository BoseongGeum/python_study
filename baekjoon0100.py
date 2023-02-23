import sys

s = sys.stdin.readline().rstrip()
s1 = set()
for x in range(len(s)):
    for y in range(x+1, len(s)+1):
        s1.add(s[x:y])
print(len(s1))
