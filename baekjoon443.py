import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    i, s = input().split()
    print(s[:int(i)-1]+s[int(i):])
