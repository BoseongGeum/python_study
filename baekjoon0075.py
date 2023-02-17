import sys

n = int(input())
l = [0]*10001
for x in range(n):
    l[int(sys.stdin.readline().rstrip())] += 1
for n in range(10001):
    for _ in range(l[n]):
        print(n)
