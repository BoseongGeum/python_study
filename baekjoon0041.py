n = int(input())
for x in range(n):
    l = list(input())
    t = 0
    o = 0
    for x in l:
        if x == "O":
            o += 1
        else:
            o = 0
        t += o
    print(t)
