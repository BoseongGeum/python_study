import sys
input = sys.stdin.readline

l = [1, 2, 3, 4, 5, 6, 7, 8]
i = list(map(int, input().split()))

if i == l:
    print("ascending")
elif i == l[::-1]:
    print("descending")
else:
    print("mixed")
