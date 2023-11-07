import sys
input = sys.stdin.readline

a, b = map(int, input().split())

length = 0
i = 1
l = []
while length < b:
    l.extend([i for _ in range(i)])
    length += i
    i += 1

print(sum(l[a-1:b]))
