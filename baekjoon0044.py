def d(n):
    l = list(str(n))
    ll = list(map(int, l))
    global total
    total = n + sum(ll)
    return total

l1 = []
l2 = []

for x in range(1, 10001):
    d(x)
    l2.append(total)
    if not x in l2:
        l1.append(x)
for x in l1:
    print(x)
