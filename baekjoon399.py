import sys
input = sys.stdin.readline

l = list(map(int, input().split()))

if l == sorted(l):
    print("Good")
else:
    print("Bad")
