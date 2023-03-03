import sys
import collections
input = sys.stdin.readline

string = input().rstrip()
q = int(input())
for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    count = collections.Counter(list(string[l:r+1]))
    print(count[a])
