import sys
input = sys.stdin.readline

s = input().rstrip()
l = 0

for i in range(len(s) // 10):
    print(s[i * 10:i * 10 + 10])
    l = i + 1
if len(s) % 10 != 0:
    print(s[l * 10:len(s)])
