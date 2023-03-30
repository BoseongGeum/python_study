u = input()
v = input()

def Prod(u, v):
    n, m = len(str(u)), len(str(v))
    c = max(n, m)
    i, j = int(u), int(v)
    
    if i == 0 and j == 0:
        return 0

    elif c <= 4:
        return i * j

    else:
        a = c // 2
        i1 = i // 10 ** (a)
        i2 = i % 10 ** (a)
        j1 = j // 10 ** (a)
        j2 = j % 10 ** (a)

        return Prod(i1, j1) * 10 ** (2 * a) + (Prod(i2, j1) + Prod(i1, j2)) * 10 ** a + Prod(i2, j2)

print(Prod(u, v))
print(int(u)*int(v))
