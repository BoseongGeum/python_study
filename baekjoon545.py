import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = str(n) * n
if n * len(str(n)) > m:
    print(answer[:m])
else:
    print(answer)
