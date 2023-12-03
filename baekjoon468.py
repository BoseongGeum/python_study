import sys
input = sys.stdin.readline

s = input().rstrip()
news = ''
for a in s:
    if a <= 'C':
        news += chr(ord(a) + 23)
    else:
        news += chr(ord(a) - 3)

print(news)
