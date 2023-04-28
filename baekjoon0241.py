import sys
input = sys.stdin.readline

l = [2]
for i in range(3, 1000000):
    for j in l:
        if i % j == 0:
            break
        if j * j > i:
            l.append(i)
            break

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 4:
        print(1)
        continue

    c = 0
    s = 1
    e = len(l) - 1
    while s <= e:
        if l[s] + l[e] > n:
            e -= 1
        elif l[s] + l[e] == n:
            e -= 1
            c += 1
            s += 1
        else:
            s += 1

    print(c)
