import sys
input = sys.stdin.readline

n = int(input())
c1 = c2 = c3 = 0

n1 = n % 300
c1 += n // 300

n2 = n1 % 60
c2 = n1 // 60

n3 = n2 % 10
c3 = n2 // 10

if n3 != 0:
    print(-1)
else:
    print(c1, c2, c3)
