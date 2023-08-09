import sys
input = sys.stdin.readline

p = 5 * int(input()) - 400

print(p)

if p > 100:
    print(-1)
elif p == 100:
    print(0)
else:
    print(1)
