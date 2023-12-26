import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    if s == 'P=NP':
        print('skipped')
        continue
    else:
        a, b = s.split('+')
        print(int(a) + int(b))
