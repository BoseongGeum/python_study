import sys

n = input()
s1 = set(sys.stdin.readline().rstrip().split())
m = int(input())
l2 = list(sys.stdin.readline().rstrip().split())

l = [1 if x in s1 else 0
     for x in l2]

print(*l, sep= ' ')
