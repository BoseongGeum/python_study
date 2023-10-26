import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    count = 0
    for i in range(n, m+1):
        count += str(i).count('0')

    print(count)
