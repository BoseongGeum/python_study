import sys
input = sys.stdin.readline

answer = [(i % 5) + 1 for i in range(10)]
n = int(input())
for j in range(1, n+1):
    p = list(map(int, input().split()))
    if p == answer:
        print(j)
