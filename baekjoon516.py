import sys
input = sys.stdin.readline

n = int(input())
while n % 2 == 0:
    n //= 2
if n == 1:
    print('1')
else:
    print('0')
