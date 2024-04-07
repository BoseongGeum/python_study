import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

asc = 0
bsc = 0
last = ''
for i in range(len(a)):
    if a[i] > b[i]:
        asc += 3
        last = 'A'
    elif a[i] < b[i]:
        bsc += 3
        last = 'B'
    else:
        asc += 1
        bsc += 1

print(asc, bsc)
if asc > bsc:
    print('A')
elif asc < bsc:
    print('B')
else:
    if asc == 10:
        print('D')
    else:
        print(last)
