import sys
input = sys.stdin.readline

t = int(input())
l = list(map(int, input().split()))
y = m = 0
for i in range(t):
    if l[i] % 60 == 59:
        m += l[i] // 60
    else:
        m += l[i] // 60 + 1
    
    if l[i] % 30 == 29:
        y += l[i] // 30
    else:
        y += l[i] // 30 + 1

y *= 10
m *= 15

if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y', 'M', y)
