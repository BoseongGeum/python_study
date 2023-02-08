c = int(input())
for x in range(c):
    n, *l = list(map(int, input().split()))
    t = 0
    ave = sum(l) / n
    for x in l:
        if x > ave:
            t += 1
    print(str("{:.3f}".format(t/n*100)+"%"))
