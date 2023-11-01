import sys
input = sys.stdin.readline

member = []
count = 0
n, k, l = map(int, input().split())
for _ in range(n):
    a = list(map(int, input().split()))
    if k <= a[0] + a[1] + a[2] and a[0] >= l and a[1] >= l and a[2] >= l:
        member.extend(a)
        count += 1
print(count)
print(*member)
