n = int(input())
al = []
for x in range(n):
    l = list(map(int, input().split()))
    al.append(l)
for x in al:
    k = 1
    for y in al:
        if x[0] < y[0] and x[1] < y[1]:
            k += 1
    x.append(k)
for x in al:
    print(x[2], end=' ')
