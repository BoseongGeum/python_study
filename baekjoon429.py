import sys
input = sys.stdin.readline
import math

dic = {'-':0, '\\':1, '(':2, '@':3, '?':4, '>':5, '&':6, '%':7, '/':-1}

while True:
    
    s = input().rstrip()
    if s == '#':
        break
    
    l = len(s) - 1
    t = 0
    
    for i in s:
        t += dic[i] * 8 ** l
        l -= 1

    print(t)
