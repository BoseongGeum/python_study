import sys
input = sys.stdin.readline

l = [0]
for i in range(1, 50):
    l += [i] * i

a, b = map(int, input().split())

result = 0
for i in range(a, b+1):
    result += l[i]

print(result)
