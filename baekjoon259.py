import sys
input = sys.stdin.readline          

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

if c >= a1 and (c - a1) * n >= a0:
    print(1)
else:
    print(0)
