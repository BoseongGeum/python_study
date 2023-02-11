n = int(input())
c = []
for x in range(n):
    a, b = input().split()
    b = list(b)
    for x in b:
        for y in range(int(a)):
            c.append(x)
    for x in c:
        print(x, end='')
    c = []
    print()
