import sys

n = input()
s1 = set(sys.stdin.readline().rstrip().split())
s2 = set(sys.stdin.readline().rstrip().split())

print(len(s1 ^ s2))
