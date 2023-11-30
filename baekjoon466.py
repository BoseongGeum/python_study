import sys
input = sys.stdin.readline

n = int(input())
l_a = sorted(list(map(int, input().split())))
l_b = sorted(list(map(int, input().split())))[::-1]

s = 0
for i in range(n):
    s += l_a[i] * l_b[i]

print(s)
