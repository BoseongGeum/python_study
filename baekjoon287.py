import sys
input = sys.stdin.readline

d = {}
n = int(input())
for _ in range(n):
    name, state = input().split()
    d[name] = state

for i in reversed(sorted(d.items())):
    if i[1] == 'enter':
        print(i[0])
