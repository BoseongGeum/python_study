import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
count = 0
for _ in range(n):
    c = input().rstrip()
    c = c * 2
    if s in c:
        count += 1

print(count)
