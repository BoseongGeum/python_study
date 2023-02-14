n = int(input())
a = 0
l = []
for x in range(int(n/5) + 1):
    b = (n - 5 * a) / 3
    if b == int(b):
        l.append(a + int(b))
    a += 1
if l == []:
    print(-1)
else:
    print(min(l))
