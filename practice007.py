u = int(input())
v = int(input())

def prod2(u, v):

    m = max(len(str(u)), len(str(v)))

    if u == v == 0:
        return 0

    elif m <= 4:
        return u * v

    else:
        h = m // 2
        u1 = u // 10 ** h
        u2 = u % 10 ** h
        v1 = v // 10 ** h
        v2 = v % 10 ** h

        r = prod2((u1 + u2), (v1 + v2))
        x = prod2(u1, v1)
        y = prod2(u2, v2)
        
        return x  * 10 ** (2*h) + (r - x - y) * 10 ** h + y

print(prod2(u, v))
