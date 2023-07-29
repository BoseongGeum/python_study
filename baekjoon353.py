import sys
input = sys.stdin.readline

n = input().rstrip()

s = 0
for i in range(5):
    s += int(n[i]) ** 5
print(s)
