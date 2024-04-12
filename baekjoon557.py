import sys
from string import ascii_uppercase
input = sys.stdin.readline

for _ in range(int(input())):
    print('Yes' if (s:=input().lower())==s[::-1] else 'No')
