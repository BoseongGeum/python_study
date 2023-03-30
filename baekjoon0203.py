import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

l = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        l.append(a[i])
        i += 1

    else:
        l.append(b[j])
        j += 1

l += a[i:]
l += b[j:]

print(*l)
