n = int(input())
l = list(map(int, input().split()))
l1 = sorted(l)
l2 = []
s = 0
for x in l1:
    x = x / l1[-1] * 100
    l2.append(x)
for x in l2:
    s += x
print(s/n)
