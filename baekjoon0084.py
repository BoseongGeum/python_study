s = [0, 1]
def pibo(n, f):
    if f < 2:
        print(s[f])
    elif n+2 == f:
        print(s[n]+s[n+1])
    else:
        s.append(s[n]+s[n+1])
        pibo(n+1, f)
f = int(input())
pibo(0, f)
