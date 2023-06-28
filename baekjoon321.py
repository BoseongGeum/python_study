import sys
input = sys.stdin.readline

n = int(input())
nl = []
for _ in range(n):
    c, s = input().split()
    s = int(s)
    if s >= 97:
        print(c, 'A+')
    elif s >= 90:
        print(c, 'A')
    elif s >= 87:
        print(c, 'B+')
    elif s >= 80:
        print(c, 'B')
    elif s >= 77:
        print(c, 'C+')
    elif s >= 70:
        print(c, 'C')
    elif s >= 67:
        print(c, 'D+')
    elif s >= 60:
        print(c, 'D')
    else:
        print(c, 'F')
