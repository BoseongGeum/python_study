import sys
input = sys.stdin.readline

def getGcd(a, b):
    while b != 0:
        rest = a % b
        a = b
        b = rest

    return a

n = int(input())

if n == 2:
    a, b = map(int, input().split())
else:
    a, b, y = map(int, input().split())

x = getGcd(max(a, b), min(a, b))

if n == 2:
    gcd = x
else:
    gcd = getGcd(max(x, y), min(x, y))

cdList = []
for i in range(1, int(gcd ** (1/2))+1):
    if gcd % i == 0:
        print(i)
        if gcd != i ** 2:
            cdList.append(i)

for i in cdList[::-1]:
    print(gcd // i)
