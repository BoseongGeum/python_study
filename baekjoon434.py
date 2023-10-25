import sys
input = sys.stdin.readline
from string import ascii_lowercase

dic = {k:0 for k in list(ascii_lowercase)}

s = input().rstrip()

for a in s:
    dic[a] += 1

print(*dic.values())
