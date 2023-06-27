import sys
input = sys.stdin.readline

l = ['A','E','I','O','U','a','e','i','o','u']

t = int(input())
for _ in range(t):
    q = input().split()
    s = ''
    for b in q:
        s += b
    i = 0
    for a in s:
        if a in l:
            i += 1
    print(len(s)-i, i)
