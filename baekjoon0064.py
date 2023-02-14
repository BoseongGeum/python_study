n = int(input())
l = list(map(int, input().split()))
for x in l:
    if x == 1:
        n -= 1
    for y in range(2, x):
        if x % y == 0:
            n -= 1
            break
print(n)
