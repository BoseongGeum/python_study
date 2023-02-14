import math

a = int(input())

n = math.ceil((2*a+1/4)**(1/2) - 1/2)
s = a - sum(range(1, n))
if n % 2 == 0:
    print(f'{s}/{n-s+1}')
else:
    print(f'{n-s+1}/{s}')
