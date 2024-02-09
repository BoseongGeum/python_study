import sys
input = sys.stdin.readline

l = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = input().split()

for w in s:
    if w not in l or w == s[0]:
        print(w[0].upper(), end='')
print()
