import sys
input = sys.stdin.readline

n = int(input())

while True:
    i = int(input())
    if i == 0:
        break
    elif i % n == 0:
        print(f"{i} is a multiple of {n}.")
    else:
        print(f"{i} is NOT a multiple of {n}.")
