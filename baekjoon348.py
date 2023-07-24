import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

c = s.count('2')
if c > n - c:
    print('2')
elif c < n - c:
    print('e') 
else:
    print('yee')
