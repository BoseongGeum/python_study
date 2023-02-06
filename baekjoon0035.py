n, x = map(int, input().split())
l1 = list(input().split())
l2 = ""

for y in l1:
    if int(y) < x:
        l2 += y+" "
print(l2)
