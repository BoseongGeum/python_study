import sys
input = sys.stdin.readline

s = input().rstrip()

l = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
for a in l:
    s = s.replace(a, '')

print(s)
