import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    if i == 0:
        print(" " * (n-1) + "*")
    elif i == n-1:
        print("*" * (i*2+1))
    else:
        print(" " * (n-1-i) + "*" + " " * (i*2-1) + "*")
