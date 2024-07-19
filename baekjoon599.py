import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
a = sorted(map(int, input().split()))


aa = a[::2] + a[::-2] if n % 2 == 0 else a[::2] + a[:-2:-2]
print(aa)
