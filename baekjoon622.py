import sys
input = sys.stdin.readline


count = {i:0 for i in range(10)}
digit = 0

n = int(input())

for i in range(10)[::-1]:
    share = n // (10 ** i)
    n = n % (10 ** i)

    if share == 0:
        continue

    print(share, n)

    digit = max(digit, i)

    for j in range(share):
        if digit == i and j == 0:
            continue
        
        count[j] += 10 ** i + share * (i-1)

    count[share] += n + 1

    print(*count.values())
