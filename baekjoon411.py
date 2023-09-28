import sys
input = sys.stdin.readline

by, bm, bd = map(int, input().split())
cy, cm, cd = map(int, input().split())

if cm > bm or (cm == bm and cd >= bd):
    print(cy - by)
else:
    print(cy - by - 1)
print(cy - by + 1)
print(cy - by)
