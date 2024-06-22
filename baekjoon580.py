import sys
input = sys.stdin.readline
import math

n = int(input())

n //= 3
n -= 3

if n < 0:
    print(0)
elif n == 0:
    print(1)
else:
    print(math.factorial((n+2))//(math.factorial(2)*math.factorial(n)))
