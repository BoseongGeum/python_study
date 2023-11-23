import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c, d, e, f, g = map(int, input().split())

s = a * b

print(f"{c - s} {d - s} {e - s} {f - s} {g - s}")
