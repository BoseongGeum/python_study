import sys
input = sys.stdin.readline

n = int(input())
a = ''

while n != 0:
    if n % 2 == 0:
        a = '0' + a
    else:
        a = '1' + a
    n //= 2
    
print(a)
