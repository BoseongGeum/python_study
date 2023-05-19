import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    print(sum(list(map(int, input().split()))))
