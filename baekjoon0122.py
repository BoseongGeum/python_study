import sys
import collections
input = sys.stdin.readline

string = input().rstrip()
q = int(input())
for _ in range(q):
    a, l, r = input().split()
    print(string[:int(r)+1].count(a) - string[:int(l)].count(a))
