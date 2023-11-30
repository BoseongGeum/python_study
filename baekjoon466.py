import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

s = set(l)

print(*sorted(s))
