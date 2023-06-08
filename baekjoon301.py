import sys
input = sys.stdin.readline

cnt = 0
while True:
    n = int(input())
    if n == 0:
        break

    n1 = n * 3
    if n1 % 2 == 1:
        n1eo = ' odd '
        n2 = (n1+1) // 2
    else:
        n1eo = ' even '
        n2 = n1 // 2

    n3 = 3 * n2
    n4 = n3 // 9
    cnt += 1

    print(str(cnt) + '.' + n1eo + str(n4))
