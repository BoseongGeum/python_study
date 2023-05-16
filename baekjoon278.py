import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
ls = len(s)

while True:
    tofls = t[-1]
    length = len(t)
    if s == t:
        print(1)
        break
    
    elif length > ls:
        t = t[:length-1]
        if tofls == 'B':
            t = t[::-1]
    else:
        print(0)
        break
