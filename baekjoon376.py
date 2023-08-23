import sys
input = sys.stdin.readline

s = input().rstrip()

hc = 0
sc = 0

for i in range(len(s)):
    if s[i] == ':' and s[i+1] == '-':
        if s[i+2] == ')':
            hc += 1
        elif s[i+2] == '(':
            sc += 1

if hc == 0 and sc == 0:
    print('none')
elif hc > sc:
    print('happy')
elif hc == sc:
    print('unsure')
else:
    print('sad')
    
