import sys
input = sys.stdin.readline

n = int(input())
l = [0] * (n + 1)

for i in range(1, n + 1):
    l[i] = int(input())
    l[i - 1] = l[i] - l[i - 1]

s = sorted(set(l[1:n-1]))
a, b = s[0], s[1]

while True:
    if a > b:
        a %= b
    else:
        b %= a
    if a == 0:
        c = b
        break
    if b == 0:
        c = a
        break

t = 0
for x in l:
    t += x // c

print(t - n + 1)
