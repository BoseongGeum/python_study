import sys
input = sys.stdin.readline

n = int(input())

l = ['' for _ in range(n)]
for i in range(n):
    l[i] = input().rstrip()

k = int(input())

if k == 1:
    for i in range(n):
        print(l[i])
elif k == 2:
    for i in range(n):
        print(l[i][::-1])
else:
    for i in reversed(range(n)):
        print(l[i])
