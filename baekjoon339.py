import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

l = [a, b, c]
s = 0

for i in l:
    if i > n:
        s += n
    else:
        s += i

print(s)
