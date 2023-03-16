import sys
input = sys.stdin.readline

k = int(input())

stack = []

for _ in range(k):
    n = int(input())
    if n == 0:
        del stack[-1]
    else:
        stack.append(n)

print(sum(stack))
