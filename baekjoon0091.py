n = int(input())
al = []
for x in range(n):
    l = list(map(int, input().split()))
    al.append(l)
al1 = list(reversed(sorted(al)))
for x in al1:
    k = 1
    for y in al1:
        if x[0] < y[0] and x[1] < y[1]:
            k += 1
    x.append(k)
print(al)
