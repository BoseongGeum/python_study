import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    l = [n]
    if n == '0':
        break
    
    while len(n) != 1:
        c = 1
        for i in range(len(n)):
            c *= int(n[i])
        l.append(c)
        n = str(c)
        
    print(*l)
