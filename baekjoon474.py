import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

aCount = 0
bCount = 0
for i in range(10):
    if a[i] > b[i]:
        aCount += 1
    elif b[i] > a[i]:
        bCount += 1

if aCount > bCount:
    print('A')
elif bCount > aCount:
    print('B')
else:
    print('D')
