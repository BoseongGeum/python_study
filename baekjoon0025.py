s = int(input())
n = int(input())
r = 0

for x in range(n):
    a, b = map(int, input().split())
    r += a * b

if r == s:
    print("Yes")
else:
    print("No")
