def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        if (a, b, c) not in d:
            d[(a, b, c)] = 1
            return 1
        else:
            return d[(a, b, c)]

    elif a > 20 or b > 20 or c > 20:
        if (a, b, c) not in d:
            d[(a, b, c)] = w(20, 20, 20)
        return w(20, 20, 20)

    elif a < b and b < c:
        if (a, b, c) not in d:
            d[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        else:
            return d[(a, b, c)]

    else:
        if (a, b, c) not in d:
            d[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        else:
            return d[(a, b, c)]
        
d = {}
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    w(a, b, c)
    print(f'w({a}, {b}, {c}) = {d[(a, b, c)]}')
