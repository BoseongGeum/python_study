import sys
input = sys.stdin.readline

n = int(input())
l = list(reversed(sorted(map(int, input().split()))))
t = 0

for x in range(n):
    t += l[x]*(x+1)

print(t)
