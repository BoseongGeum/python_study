import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    result = 0
    c = list(map(int, input().split()))
    for i in c:
        result += i // k
    print(result)
