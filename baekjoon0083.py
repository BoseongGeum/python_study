def fac(n, s):
    if n == 0:
        print(s)
    else:
        s *= n
        fac(n - 1, s)
n = int(input())
fac(n, 1)
