import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
l = sorted(list(map(int, input().split())))

a = 0
b = n - 1
c = 0
while a < b:
    if l[b] > m:
        b -= 1
    elif l[a] + l[b] > m:
        b -= 1
    elif l[a] + l[b] < m:
        a += 1
    else:
        a += 1
        b -= 1
        c += 1

print(c)
