import sys
input = sys.stdin.readline

l = []
for j in range(5):
    n = input().rstrip()
    for i in range(len(n) - 2):
        if n[i:i+3] == 'FBI':
            l.append(j + 1)
            break

if len(l) == 0:
    print('HE GOT AWAY!')
else:
    print(*l)
