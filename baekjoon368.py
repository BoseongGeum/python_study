import sys
input = sys.stdin.readline

l = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
while True:
    s = input().rstrip()
    if s == '#':
        break
    c = 0
    for a in s:
        if a in l:
            c += 1
            
    print(c)
