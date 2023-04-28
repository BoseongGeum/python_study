import sys
input = sys.stdin.readline

n = int(input())

if n < 3:
    print(1)

else:
    for i in range(1, n):
        if i ** 2 > n:
            print(i - 1)
            break
