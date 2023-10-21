import sys
input = sys.stdin.readline

a = 1
for _ in range(3):
    a *= int(input())

for i in range(10):
    print(str(a).count(str(i)))
