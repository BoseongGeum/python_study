import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(list(map(int, input().split()))))
