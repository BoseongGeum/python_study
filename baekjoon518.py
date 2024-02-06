import sys
input = sys.stdin.readline

t = int(input())
l = [''] * t
for i in range(t):
    l[i] = input().rstrip()

if l == sorted(l):
    print('INCREASING')
elif l == sorted(l)[::-1]:
    print('DECREASING')
else:
    print('NEITHER')
