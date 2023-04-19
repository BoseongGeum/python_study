import sys
input = sys.stdin.readline

a = [0] * 3
for i in range(3):
    a[i] = int(input())

if sum(a) != 180:
    print('Error')
    
else:
    if a[0] == a[1] == a[2]:
        print('Equilateral')
    elif a[0] != a[1] and a[1] != a[2] and a[2] != a[0]:
        print('Scalene')
    else:
        print('Isosceles')
