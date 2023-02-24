import sys
input = sys.stdin.readline

n = int(input())

s1 = {int(input()) for _ in range(n)}
c = sorted(list(s1))[1] - 1
f = 2

while True:    
    s2 = set()
    for x in s1:
        y = x % c
        s2.add(y)
        if len(s2) == 2:
            break
    if len(s2) == 1:
        break
    c -= 1

l = [c]            
while True:
    if f > c//f:
        break
    elif c % f == 0:
        if f == c//f:
            l.append(f)
            break
        else:
            l.extend([f, c//f])
    f += 1

print(*sorted(l))
