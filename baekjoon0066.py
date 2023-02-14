n = int(input())

for x in range(2, n):
    while True:
        if n % x == 0:
            print(x)
            n = n / x
        else:
            break
if n == n and n != 1:
    print(n)
