import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())
count = 0
for _ in range(n):
    c = input().rstrip()
    exist = False
    for a in s:
        if not a in c:
            exist = True
            break
    if exist:
        count += 1
