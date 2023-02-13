a = int(input())
f = 6
n = 1
g = f*n
while True:
    if a > 1 + g:
        n += 1
        g += f*n
    elif a == 1:
        print(a)
        break
    else:
        print(n+1)
        break
