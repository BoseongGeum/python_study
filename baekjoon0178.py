import sys
input = sys.stdin.readline

a = 0

for _ in range(5):
    s = int(input())

    if s < 40:
        s = 40

    a += s

print(a//5)
