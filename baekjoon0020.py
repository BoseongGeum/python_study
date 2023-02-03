a, b = map(int, input().split())
c = int(input())
e = c % 60
d = c // 60

if b + e >= 60:
    a += 1
    g = (b + e) % 60
else:
    g = b + e

if a + d >= 24:
    f = (a + d) % 24
else:
    f = a + d

print(f,g)
